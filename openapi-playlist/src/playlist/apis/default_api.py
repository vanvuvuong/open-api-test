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

from playlist.models.extra_models import TokenModel  # noqa: F401
from playlist.models.playlist import Playlist


router = APIRouter()


@router.delete(
    "/playlist",
    responses={
        200: {"model": Playlist, "description": "Success"},
        400: {"model": str, "description": "Invalid Request"},
    },
    tags=["default"],
    summary="Delete the artist data",
)
async def playlist_delete(
    category_id: int = Query(None, description="Delete data depend on category ID "),
    id: int = Query(None, description="Delete data depend on the ID"),
    name: str = Query(None, description="Delete data depend on artist full name"),
) -> Playlist:
    ...


@router.get(
    "/playlist",
    responses={
        200: {"model": Playlist, "description": "Sucessfull response"},
        404: {"model": str, "description": "Invalid request"},
    },
    tags=["default"],
    summary="Getting all the playlist data (default limit is 20)",
)
async def playlist_get(
    category_id: int = Query(None, description="Get the data from an Category ID"),
    id: int = Query(None, description="Get the data from an ID"),
    since_id: int = Query(None, description="Get the data from ID bigger than the ID you provide"),
    limit: int = Query(None, description="The number of the data you can get"),
    created_at_min: str = Query(None, description="Get the data from specfic creating time"),
    created_at_max: str = Query(None, description="Get the data to specfic creating time"),
) -> Playlist:
    """Getting all the playlist data (default limit is 20) Specific for those fields:&lt;br/&gt;**Category ID**&lt;br/&gt;**ID**&lt;br/&gt;**Name: **&lt;br/&gt;**URL**"""
    ...


@router.post(
    "/playlist",
    responses={
        200: {"model": Playlist, "description": "Sucessfull response"},
        400: {"model": str, "description": "Invalid Request"},
    },
    tags=["default"],
    summary="Creating the playlist data",
)
async def playlist_post(
    category_id: int = Query(None, description="The Category ID to get the data from"),
    name: str = Query(None, description="Playlist name"),
    url: str = Query(None, description="Artist link URL"),
) -> Playlist:
    """Creating the new playlist data, and send it to the server"""
    ...


@router.put(
    "/playlist",
    responses={
        200: {"model": Playlist, "description": "Sucessfull response"},
        400: {"model": str, "description": "Invalid Request"},
    },
    tags=["default"],
    summary="Update the artist data",
)
async def playlist_put(
    category_id: int = Query(None, description="The Category ID to get the data from"),
    name: str = Query(None, description="Playlist name"),
    url: str = Query(None, description="Artist link URL"),
) -> Playlist:
    ...
