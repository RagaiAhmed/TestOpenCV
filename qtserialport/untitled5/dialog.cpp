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
    QString str = ui->lineEdit->text();
    Dialog::updateleds(QString("R%1").arg(str));
    qDebug() << str;
    QString str2 = ui->lineEdit_2->text();
    Dialog::updateleds(QString("B%1").arg(str2));
    qDebug() << str2;
    //QString str = "R" + ui->lineEdit->text() + "B" + ui->lineEdit_2->text();
    //Dialog::updateleds(str);
    //QMessageBox::information(this, "Title", str);
}


void Dialog::on_pushButton_2_clicked()
{
    Dialog::updateleds("S");

}
void Dialog::updateleds(QString command)
{

    //QMessageBox::information(this, "Title", command.toStdString().c_str());

    if(arduino->isWritable()){
        arduino->write(command.toStdString().c_str());
    }
    else
    {
        qDebug() << "Couldn't write to serial!";
    }
}
