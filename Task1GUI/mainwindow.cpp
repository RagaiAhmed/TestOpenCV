#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>
#include <QDebug>
#include <QtWidgets>
//#include <QSerialPort>
#include <QtSerialPort/QSerialPort>
#include <QtSerialPort/QSerialPortInfo>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    arduino_is_available = false;
    arduino_port_name = "";
    arduino = new QSerialPort ;

    /*
    qDebug() << "Number of available ports: " << QSerialPortInfo::availablePorts().length();
    foreach(const QSerialPortInfo &serialPortInfo, QSerialPortInfo::availablePorts()){
        qDebug() << "Has vendor ID: " << serialPortInfo.hasVendorIdentifier();
        if(serialPortInfo.hasVendorIdentifier()){
            qDebug() << "Vendor ID: " << serialPortInfo.vendorIdentifier();
        }
        qDebug() << "Has Product ID: " << serialPortInfo.hasProductIdentifier();
        if(serialPortInfo.hasProductIdentifier()){
            qDebug() << "Product ID: " << serialPortInfo.productIdentifier();
        }
    }
    */

    foreach(const QSerialPortInfo &serialPortInfo, QSerialPortInfo::availablePorts()){
            if(serialPortInfo.hasVendorIdentifier() && serialPortInfo.hasProductIdentifier()){
                if(serialPortInfo.vendorIdentifier() == arduino_uno_vendor_id){
                    if(serialPortInfo.productIdentifier() == arduino_uno_product_id){
                        arduino_port_name = serialPortInfo.portName();
                        arduino_is_available = true;
                    }
                }
            }
        }

        if(arduino_is_available){
            // open and configure the serialport
            arduino->setPortName(arduino_port_name);
            arduino->open(QSerialPort::WriteOnly);
            arduino->setBaudRate(QSerialPort::Baud9600);
            arduino->setDataBits(QSerialPort::Data8);
            arduino->setParity(QSerialPort::NoParity);
            arduino->setStopBits(QSerialPort::OneStop);
            arduino->setFlowControl(QSerialPort::NoFlowControl);
        }
        else{
            // give error message if not available
            QMessageBox::warning(this, "Port error", "Couldn't find the Arduino!");
        }

}

MainWindow::~MainWindow()
{
    if(arduino->isOpen()){
            arduino->close();
        }

    delete ui;
}


void MainWindow::on_onButton_clicked()
{
    //QMessageBox::information(this,"Title",ui->lineEditRed->text() + ui->lineEditBlue->text());
    value = 'r' + ui->lineEditRed->text() + 'b' + ui->lineEditBlue->text();
    MainWindow::updateBlinkStatus(value);
    qDebug() << value;

}

void MainWindow::on_offButton_clicked()
{
    value = 's';
    MainWindow::updateBlinkStatus(value);
    qDebug() << value;
}

void MainWindow::updateBlinkStatus(QString command)
{
    if(arduino->isWritable()){
        arduino->write(command.toStdString().c_str());
    }
    else{
        qDebug() << "Couldn't write to serial!";
    }
}
