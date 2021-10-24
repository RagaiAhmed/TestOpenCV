#include "dialog.h"
#include "ui_dialog.h"
#include <QSerialPort>
#include <QSerialPortInfo>
#include <QDebug>
#include <QtWidgets>
#include <QtCore>
#include <QtGui>

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Dialog)
{
    ui->setupUi(this);

    arduino_is_available = false;
       arduino_port_name = "";
       arduino = new QSerialPort;

       // to know vendor id and product id of the arduino connected
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
       }else{
           // give error message if not available
           QMessageBox::warning(this, "Port error", "Couldn't find the Arduino!");
       }


}

Dialog::~Dialog()
{
    if(arduino->isOpen()){
            arduino->close();
        }
    delete ui;
}


void Dialog::on_pushButton_clicked()
{

    QString on = "R" + ui->lineEdit->text() + "B" + ui->lineEdit_2->text();
    Dialog::updateleds(on);

}


void Dialog::on_pushButton_2_clicked()
{
    QString off = "S";
    Dialog::updateleds(off);

}
void Dialog::updateleds(QString str)
{

    //QMessageBox::information(this, "info", str.toStdString().c_str());

    if(arduino->isWritable()){
        arduino->write(str.toStdString().c_str());
    }
    else
    {
        qDebug() << "Couldn't write to serial!";
    }
}
