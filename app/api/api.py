from fastapi import APIRouter


from .endpoints.testEndpoint import router as test_endpoint

router = APIRouter()

router.include_router(test_endpoint)