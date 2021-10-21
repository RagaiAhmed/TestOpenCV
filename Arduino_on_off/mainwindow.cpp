#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , serial(new QSerialPort(this))
    ,  ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    serial->setBaudRate (QSerialPort::Baud9600);
    serial->setDataBits(QSerialPort::Data8);
    serial->setParity (QSerialPort::NoParity);
    serial->setStopBits (QSerialPort::OneStop);
    serial->setFlowControl(QSerialPort::NoFlowControl);


}

MainWindow::~MainWindow()
{
    delete ui;

}

void MainWindow::on_pushButton_clicked()
{
   serial->setPortName(ui->lineEdit->text());
    serial->open(QIODevice::WriteOnly);
}


void MainWindow::on_pushButton_on_clicked()
{
        buffer = 'R'+ ui->redLineEdit->text() +'B'+ ui->blueLineEdit->text() ;
        serial->write((char*)buffer.data());
        qDebug()<< buffer;

}


void MainWindow::on_pushButton_off_clicked()
{
     buffer = 'S' ;
    serial->write((char*)buffer.data());
    qDebug()<< buffer;
}





