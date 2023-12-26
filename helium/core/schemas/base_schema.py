import enum
import typing
from collections import namedtuple
from pydantic import BaseModel, ConfigDict
from helium.core.database.methods import save_model_to_db, ModelPair


__PRITIMIVE_TYPES__ = [str, int, float, bool, list, dict, enum.EnumType]
__DECLARED_TYPES__ = [typing._GenericAlias]


class BaseModelSchema(BaseModel):
    __orm_model__: object

    model_config = ConfigDict(
        from_attributes=True,
    )

    @staticmethod
    def _build_orm_objects(data):
        if not data:
            return
        for key, value in data.model_fields.items():
            annotation = getattr(value, "annotation")
            if type(annotation) == enum.EnumType:
                continue
            if (
                annotation not in __PRITIMIVE_TYPES__
                and type(annotation) not in __DECLARED_TYPES__
            ):
                orm_model = BaseModelSchema._build_orm_objects(
                    getattr(data, key)
                )
                setattr(data, key, orm_model)
            elif type(annotation) in __DECLARED_TYPES__:
                items_list = []
                for item in getattr(data, key):
                    orm_model = BaseModelSchema._build_orm_objects(item)
                    items_list.append(orm_model)
                setattr(data, key, orm_model)
        return data.__orm_model__(**vars(data))

    @save_model_to_db
    def save(self):
        db_obj = self._build_orm_objects(self)
        return ModelPair(db_model=db_obj, schema=self)
