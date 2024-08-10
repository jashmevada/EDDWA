from db.db import db

from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, auto_increment=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(unique=True)


class Flood(db.Model):
    id: Mapped[str] = mapped_column(ForeignKey(User.username),primary_key=True)
    longitude: Mapped[str] = mapped_column()
    latitude: Mapped[str] = mapped_column()
    probability: Mapped[float] = mapped_column()


class ForestFire(db.Model):
    id: Mapped[int] = mapped_column(ForeignKey(User.username),primary_key=True)
    longitude: Mapped[str] = mapped_column()
    latitude: Mapped[str] = mapped_column()
    probability: Mapped[float] = mapped_column()


class LandSlide(db.Model):
    id: Mapped[int] = mapped_column(ForeignKey(User.username),primary_key=True)
    longitude: Mapped[str] = mapped_column()
    latitude: Mapped[str] = mapped_column()
    probability: Mapped[float] = mapped_column()
