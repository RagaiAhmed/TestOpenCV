#include "dialog.h"
#include "ui_dialog.h"
#include<QSerialPort>
#include<QSerialPortInfo>
#include<QDebug>

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Dialog)
{
    ui->setupUi(this);
    arduino = new QSerialPort;

     /* qDebug() << "Number of available ports: " << QSerialPortInfo::availablePorts().length();
      foreach(const QSerialPortInfo &serialPortInfo, QSerialPortInfo::availablePorts()){
          qDebug() << "Has vendor ID: " << serialPortInfo.hasVendorIdentifier();
          if(serialPortInfo.hasVendorIdentifier()){
              qDebug() << "Vendor ID: " << serialPortInfo.vendorIdentifier();
          }
          qDebug() << "Has Product ID: " << serialPortInfo.hasProductIdentifier();
          if(serialPortInfo.hasProductIdentifier()){
              qDebug() << "Product ID: " << serialPortInfo.productIdentifier();
          }
      }*/

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
}

Dialog::~Dialog()
{
    delete ui;
}


void Dialog::on_pushButton_2_clicked()
{
     QString command = QString("r%1b%2").arg(ui->lineEdit->text()).arg(ui->lineEdit_2->text());
    Dialog::blink_led(command);
    qDebug()<<command;

}


void Dialog::on_pushButton_clicked()
{
  Dialog::turn_off_leds();
}

void Dialog::blink_led(QString command)
{
    if(arduino->isWritable()){
        arduino->write(command.toStdString().c_str());
    }else{
        qDebug() << "Couldn't write to serial!";
    }
}
void Dialog::turn_off_leds()
{   QString command ="s";
    if(arduino->isWritable()){
        arduino->write(command.toStdString().c_str());
    }else{
        qDebug() << "Couldn't write to serial!";
    }
}

