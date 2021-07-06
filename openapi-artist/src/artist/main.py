# coding: utf-8

"""
    Nhaccuatui Music Data

    Get the nhaccuatui.com data from the database. After crawling data

    The version of the OpenAPI document: 1.0
    Contact: vanvuvuong3@gmail.com
    Generated by: https://openapi-generator.tech
"""


from fastapi import FastAPI

from artist.apis.default_api import router as DefaultApiRouter

app = FastAPI(
    title="Nhaccuatui Music Data",
    description="Get the nhaccuatui.com data from the database. After crawling data",
    version="1.0",
)

app.include_router(DefaultApiRouter)
