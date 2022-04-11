from sqlalchemy import create_engine
from WeGo.settings import settings

engine = create_engine(
    settings.db_url,
)

