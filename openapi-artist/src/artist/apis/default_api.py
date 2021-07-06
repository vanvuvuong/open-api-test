# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from artist.models.extra_models import TokenModel  # noqa: F401
from artist.models.artist import Artist


router = APIRouter()


@router.delete(
    "/artist",
    responses={
        200: {"model": Artist, "description": "Success"},
        400: {"model": str, "description": "Invalid Request"},
    },
    tags=["default"],
    summary="Delete the artist data",
)
async def artist_delete(
    source_id: int = Query(None, description="Delete data depend on source ID "),
    id: int = Query(None, description="Delete data depend on the ID"),
    name: str = Query(None, description="Delete data depend on artist full name"),
) -> Artist:
    ...


@router.get(
    "/artist",
    responses={
        200: {"model": Artist, "description": "Sucessfull response"},
        404: {"model": str, "description": "Invalid request"},
    },
    tags=["default"],
    summary="Getting all the artist data (default limit is 20)",
)
async def artist_get(
    id: int = Query(None, description="Get the data from an ID"),
    source_id: int = Query(None, description="Get the data from an source ID"),
    since_id: int = Query(None, description="Get the data from ID bigger than the ID you provide"),
    limit: int = Query(None, description="The number of the data you can get"),
    created_at_min: str = Query(None, description="Get the data from specfic creating time"),
    created_at_max: str = Query(None, description="Get the data to specfic creating time"),
    nationality: str = Query(None, description="Get the data by nationality"),
) -> Artist:
    """Getting all the artist data. Specific for those fields:&lt;br/&gt;**ID**&lt;br/&gt;**Name: **&lt;br/&gt;**Nationality**&lt;br/&gt;**URL**"""
    ...


@router.post(
    "/artist",
    responses={
        200: {"model": Artist, "description": "Sucessfull response"},
        400: {"model": str, "description": "Invalid Request"},
    },
    tags=["default"],
    summary="Creating the artist data",
)
async def artist_post(
    source_id: int = Query(None, description="The Source ID to get the data from"),
    name: str = Query(None, description="Artist Full Name"),
    birthday: str = Query(None, description="Date of birth"),
    gender: str = Query(None, description="Gender"),
    life: str = Query(None, description="Brief description about artist life"),
    url: str = Query(None, description="Artist link URL"),
) -> Artist:
    """Creating the new artist data, and send it to the server"""
    ...


@router.put(
    "/artist",
    responses={
        200: {"model": Artist, "description": "Sucessfull response"},
        400: {"model": str, "description": "Invalid Request"},
    },
    tags=["default"],
    summary="Update the artist data",
)
async def artist_put(
    source_id: int = Query(None, description="The Source ID to get the data from"),
    name: str = Query(None, description="Artist Full Name"),
    birthday: str = Query(None, description="Date of birth"),
    gender: str = Query(None, description="Gender"),
    life: str = Query(None, description="Brief description about artist life"),
    url: str = Query(None, description="Artist link URL"),
) -> Artist:
    ...
