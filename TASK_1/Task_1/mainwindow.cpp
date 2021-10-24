#include "mainwindow.h"
#include "ui_mainwindow.h"

#include "QTextStream"
#include "QSerialPort"
#include "QSerialPortInfo"
#include "QDebug"

#include "iostream"
using namespace std;


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    arduino = new QSerialPort;

    foreach(const QSerialPortInfo &serialPortInfo, QSerialPortInfo::availablePorts()){
        if(serialPortInfo.hasVendorIdentifier() && serialPortInfo.hasProductIdentifier()){
            if(serialPortInfo.vendorIdentifier() == arduino_vendor_id){
                if(serialPortInfo.productIdentifier() == arduino_product_id){
                    arduino_port_name = serialPortInfo.portName();
                    arduino_is_available = true;
                }
            }
        }
    }
    arduino_is_available = false;
    arduino_port_name = "";

    if(arduino_is_available)
    {arduino = new QSerialPort;
        arduino->setPortName(arduino_port_name);
        arduino->open(QSerialPort::WriteOnly);
        arduino->setBaudRate(QSerialPort::Baud9600);
        arduino->setDataBits(QSerialPort::Data8);
        arduino->setParity(QSerialPort::NoParity);
        arduino->setStopBits(QSerialPort::OneStop);
        arduino->setFlowControl(QSerialPort::NoFlowControl);
    }

}

MainWindow::~MainWindow()
{
    if(arduino->isOpen()){
        arduino->close();
    }
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    QTextStream output(stdout);
    command = "R";
    cout<<"ON"<<endl;
    redLED = ui->lineEdit->displayText();
    blueLED = ui->lineEdit_2->displayText();
    command.append(redLED);
    command.append("B");
    command.append(blueLED);
    output<<command<<"\n";
    updateLED(command);


}
void MainWindow::on_pushButton_2_clicked()
{
    QTextStream output(stdout);
    cout<<"OFF"<<endl;
    command = "S";
    output<<command<<"\n";
    updateLED(command);

}
void MainWindow::updateLED(QString command)
{
    if(arduino->isWritable()){
        arduino->write(command.toStdString().c_str());
    }
}
