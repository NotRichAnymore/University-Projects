#ifndef MYPHPDATABASE_H
#define MYPHPDATABASE_H


#include <QtSql>
#include <QSqlDatabase>

//details for the database connection
#define SQLDB "QMYSQL"
#define HOST "127.0.0.1"
#define USER "admin"
#define PASSWORD "o8rvjZklPNOG"
#define DB_NAME "etmDatabase"



class myphpdatabase
{
private:
    QSqlDatabase database;
    bool check=false;

public:
    void init_database(void);
    QSqlDatabase get_database(void);
    bool database_status(void);
    myphpdatabase();
    ~myphpdatabase();
};

#endif // MYPHPDATABASE_H
