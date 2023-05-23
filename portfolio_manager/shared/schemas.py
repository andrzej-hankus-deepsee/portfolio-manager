import inflection
from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        use_enum_values = True
        allow_population_by_field_name = True

        @classmethod
        def alias_generator(cls, string: str) -> str:
            return inflection.camelize(string, False)


class SuccessSchema(BaseSchema):
    success: bool = True