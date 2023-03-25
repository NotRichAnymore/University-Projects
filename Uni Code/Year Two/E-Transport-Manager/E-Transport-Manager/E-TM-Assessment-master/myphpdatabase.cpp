#include "myphpdatabase.h"

myphpdatabase::myphpdatabase()
{
    myphpdatabase::init_database();
}


myphpdatabase::~myphpdatabase()
{
    if(!myphpdatabase::check)
    {

        myphpdatabase::database.close();
    }
}

bool myphpdatabase::database_status(void)
{
     return myphpdatabase::check;
}


void myphpdatabase::init_database(void)
{
    myphpdatabase::database = QSqlDatabase::addDatabase(SQLDB);
    myphpdatabase::database.setHostName(HOST);
    myphpdatabase::database.setUserName(USER);
    myphpdatabase::database.setPassword(PASSWORD);
    myphpdatabase::database.setDatabaseName(DB_NAME);
    myphpdatabase::database.open();
    myphpdatabase::check=true;
}

QSqlDatabase myphpdatabase :: get_database()
{
    if(!myphpdatabase::check)
    {
        myphpdatabase::init_database();
    }
    return myphpdatabase::database;
}


