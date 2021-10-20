#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QCoreApplication>

#include <QtSerialPort/QSerialPort>
#include <QtSerialPort/QSerialPortInfo>
#include <QDebug>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    serial = new QSerialPort;

    int ports = QSerialPortInfo::availablePorts().length();

    for(int i = 0; i < ports; i++)
    {
        const QSerialPortInfo &port_info = QSerialPortInfo::availablePorts().at(i);
        if(port_info.hasVendorIdentifier() && port_info.hasProductIdentifier())
        {
            if(port_info.vendorIdentifier() == 0x2341 && port_info.productIdentifier() == 0x43)
            {
                port = port_info.portName();
            }
        }
    }

    serial->setPortName(port);
    serial->open(QSerialPort::WriteOnly);
    serial->setBaudRate(QSerialPort::Baud9600);
    serial->setDataBits(QSerialPort::Data8);
    serial->setParity(QSerialPort::NoParity);
    serial->setStopBits(QSerialPort::OneStop);
    serial->setFlowControl(QSerialPort::NoFlowControl);
    qDebug() << port;
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    QString red = ui->lineEdit->text();
    QString blue = ui->lineEdit_2->text();

    QString message = "R" + red + "B" + blue;

    if(serial->isWritable())
    {
        serial->write(message.toStdString().c_str());
        qDebug() << message;
    }
}


void MainWindow::on_pushButton_2_clicked()
{
    QString message = "S";

    if(serial->isWritable())
    {
        serial->write(message.toStdString().c_str());
        qDebug() << message;
    }
}

