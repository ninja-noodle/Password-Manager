from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import secrets
from string import ascii_letters, digits, punctuation

class Base(DeclarativeBase):
    pass


class Credential(Base):
    __tablename__ = "credential"

    id: Mapped[int] = mapped_column(primary_key=True)
    service: Mapped[str] = mapped_column(String(100)) 
    url: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    identifier: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(255))
    notes: Mapped[Optional[str]] = mapped_column(nullable=True)


class MasterKey(Base):
    __tablename__ = "master_key"

    id: Mapped[int] = mapped_column(primary_key=True)
    hashed_key: Mapped[str] = mapped_column(String(255), nullable=False)


class VaultCore(Base):
    __tablename__ = "vault_core"

    id: Mapped[int] = mapped_column(primary_key=True)
    encrypted_fernet_key: Mapped[str] = mapped_column(String(255), nullable=False)
    salt: Mapped[str] = mapped_column(String(255), nullable=False)
