#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    serial = new QSerialPort();
    arduino_available = false;
    foreach(const QSerialPortInfo &serial_info,QSerialPortInfo::availablePorts() ){
        qDebug()<<"port: " <<serial_info.portName();
        portname= serial_info.portName();
         qDebug()<<"Vendor Id: " <<serial_info.vendorIdentifier();
         vendorId= serial_info.vendorIdentifier();
          qDebug()<<"Product Id: " <<serial_info.productIdentifier();
          productId=serial_info.productIdentifier();
          arduino_available=true;
    }
    if(arduino_available){
            arduino_init();
        }
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::arduino_init()
{
    serial->setPortName(portname);
    serial->setBaudRate(QSerialPort::Baud9600);
    serial->setDataBits(QSerialPort::Data8);
        serial->setParity(QSerialPort::NoParity);
        serial->setStopBits(QSerialPort::OneStop);
        serial->setFlowControl(QSerialPort::NoFlowControl);
        serial->open(QIODevice::ReadWrite);
}


void MainWindow::on_pushButton_clicked()
{
    QString blinkRate = "R"+ui->lineEdit->text()+"B"+ui->lineEdit_2->text();
    if(serial->isWritable()){
            serial->write(blinkRate.toStdString().c_str(),blinkRate.size());
        }
}


void MainWindow::on_pushButton_2_clicked()
{
    if(serial->isWritable()){
            serial->write("S");
        }
}

