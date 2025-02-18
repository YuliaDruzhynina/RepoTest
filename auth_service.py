
from app.database.models import Image, Role, User
from app.database.connection import get_db
from app.schemas import ImageCreate, ImageResponseSchema
from app.services.auth_service import get_current_user   #зробити корректн import!
from app.settings import settings

router = APIRouter(tags=['images'])

cloudinary.config(
    cloud_name=settings.CLD_NAME, 
    api_key=settings.CLD_API_KEY,   
    api_secret=settings.CLD_API_SECRET  #add to .env!# logic auth (jwt, hashing passw)
