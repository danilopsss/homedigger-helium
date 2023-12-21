from pydantic import BaseModel, ConfigDict
from helium.core.database.methods import save_model_to_db


__PRITIMIVE_TYPES__ = [str, int, float, bool, list, dict]


class BaseModelSchema(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    @staticmethod
    def _build_orm_objects(data):
        if not data:
            return
        for key, value in data.model_fields.items():
            if not getattr(value, "annotation") in __PRITIMIVE_TYPES__:
                orm_model = BaseModelSchema._build_orm_objects(getattr(data, key))
                setattr(data, key, orm_model)
        return data.__orm_model__(**vars(data))


    @save_model_to_db
    def save_to_database(self):
        return self._build_orm_objects(self)
