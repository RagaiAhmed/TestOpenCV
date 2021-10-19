#include "dialog.h"
#include "ui_dialog.h"
#include <QDebug>
#include <QSerialPort>
#include <QSerialPortInfo>
#include <QtWidgets>

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Dialog)
{
    ui->setupUi(this);
    arduino_port_name = "";
    arduino_is_available = false;
    arduino = new QSerialPort;
    foreach(const QSerialPortInfo &serialPortInfo, QSerialPortInfo::availablePorts()){
        if(serialPortInfo.hasVendorIdentifier() && serialPortInfo.hasProductIdentifier()){
            if(serialPortInfo.vendorIdentifier()==arduino_uno_vendor_id){
                if(serialPortInfo.productIdentifier()==arduino_uno_product_id){
                    arduino_port_name = serialPortInfo.portName();
                    arduino_is_available = true;

                }
            }
        }
    }
    if(arduino_is_available){
        arduino->setPortName(arduino_port_name);
        arduino->open(QSerialPort::WriteOnly);
        arduino->setBaudRate(QSerialPort::Baud9600);
        arduino->setDataBits(QSerialPort::Data8);
        arduino->setParity(QSerialPort::NoParity);
        arduino->setStopBits(QSerialPort::OneStop);
        arduino->setFlowControl(QSerialPort::NoFlowControl);

    }else{
        QMessageBox::warning(this,"warning","couldnt find the arduino");

    }




}

Dialog::~Dialog()
{ if(arduino->isOpen())
        arduino->close();
    delete ui;
}
QString result="";

void Dialog::on_pushButton_clicked(){
 QString red = ui->lineEdit->text();
 QString blue = ui->lineEdit_2->text();
 QString result = "R"+red+"B"+blue;
    qDebug() << result;
    sendMESSAGE(result);
}


void Dialog::on_pushButton_2_clicked()
{
     sendMESSAGE("S");

}
void Dialog::sendMESSAGE(QString result){
    if(arduino->isWritable()){
        arduino->write(result.toStdString().c_str());
    }
    else
         QMessageBox::information(this,"info","couldnt write on serial");

}
