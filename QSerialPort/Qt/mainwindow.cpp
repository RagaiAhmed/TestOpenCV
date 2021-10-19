#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    serial = new QSerialPort();
    arduino_available = false;

    foreach (const QSerialPortInfo &serial_Info, QSerialPortInfo::availablePorts()) {
        portname = serial_Info.portName();
        vendorId = serial_Info.vendorIdentifier();
        productId = serial_Info.productIdentifier();
        arduino_available = true;
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
    serial->setBaudRate (QSerialPort::Baud9600);
    serial->setDataBits(QSerialPort::Data8);
    serial->setParity (QSerialPort::NoParity);
    serial->setStopBits (QSerialPort::OneStop);
    serial->setFlowControl(QSerialPort::NoFlowControl);
    serial->open(QIODevice::ReadWrite);
}

void MainWindow::on_OnButton_clicked()
{
    QString code = "R"+ui->RedlineEdit->text()+"B"+ui->BluelineEdit->text();
    if(serial->isWritable()){
        serial->write(code.toStdString().c_str(), code.size());
    }
}


void MainWindow::on_OffButton_clicked()
{
    if(serial->isWritable()){
        serial->write("S");
    }
}

