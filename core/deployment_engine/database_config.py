from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass

class Schema(Base):

    _tablename_ = "schema"

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(30))
    version:Mapped[str] = mapped_column(String(30))
    version:Mapped[str] = mapped_column(String(30))

    runtimeEnvironment: Mapped[str] = mapped_column(String(30))
    requiredPlatform: Mapped[str] = mapped_column(String(30))
    run_containerized: Mapped[bool] = mapped_column(bool)

    dependecies: Mapped[str] = mapped_column(String(30))

    subsTopic: Mapped[str] = mapped_column(String(30))

    Pubs_Topic: Mapped[str] = mapped_column(String(30))


    mode: Mapped[str] = mapped_column(String(30))
    execCommands: Mapped[str] = mapped_column(String(30))

    waitForExit: Mapped[str] = mapped_column(String(30))


    status: Mapped[str] = mapped_column(String(30))

    deInternalStatus: Mapped[str] = mapped_column(String(30))





class Process(Base):
    _tablename_ = "stats"

    id: Mapped[int] = mapped_column(ForeignKey("schema.id"))
    cmd: Mapped[str] = mapped_column(String(30))
    status: Mapped[str] = mapped_column(String(30))
    statusInfo: Mapped[str] = mapped_column(String(30))


class Stats(Base):
    _tablename_ = "stats"

    id: Mapped[int] = mapped_column(ForeignKey("schema.id"))
    msgPublished: Mapped[int] = mapped_column(int)
    msgSentToOpp: Mapped[int] = mapped_column(int)
    resourceUsage: Mapped[float] = mapped_column(float)



