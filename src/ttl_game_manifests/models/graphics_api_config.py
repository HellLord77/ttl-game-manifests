from .base import Base
from .graphics_api_option import GraphicsApiOption


class GraphicsApiConfig(Base):
    options: list[GraphicsApiOption]
    default: str
