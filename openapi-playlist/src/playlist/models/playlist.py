# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class Playlist(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Playlist - a model defined in OpenAPI

        category_id: The category_id of this Playlist [Optional].
        id: The id of this Playlist [Optional].
        name: The name of this Playlist [Optional].
        url: The url of this Playlist [Optional].
    """

    category_id: Optional[int] = None
    id: Optional[int] = None
    name: Optional[str] = None
    url: Optional[str] = None

Playlist.update_forward_refs()
