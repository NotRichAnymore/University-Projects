QT += core sql
QT -= gui

CONFIG += console c++11
CONFIG -= app_bundle
DEFINES += QT_DEPRECATED_WARNINGS

SOURCES += \
        etmcargo.cpp \
        etmdriver.cpp \
        etmorder.cpp \
        etmtransportc.cpp \
        main.cpp \
        myphpdatabase.cpp

HEADERS += \
    etmcargo.h \
    etmdriver.h \
    etmorder.h \
    etmtransportc.h \
    myphpdatabase.h
