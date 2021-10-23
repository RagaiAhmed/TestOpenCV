#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QSerialPort>
#include <QSerialPortInfo>
#include <QDebug>
#include <QtWidgets>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    arduino_is_available = false;
    arduino_port_name = "";
    arduino = new QSerialPort;

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

MainWindow::~MainWindow()
{
    if(arduino->isOpen()){
            arduino->close();
        }
        delete ui;
}


void MainWindow::on_redbutton_pressed()
{
    val = 'R' + ui->red->text();
    MainWindow::Blink(val);
    qDebug() << val;
}

void MainWindow::on_bluebutton_pressed()
{
    val = 'B' + ui->blue->text();
    MainWindow::Blink(val);
    qDebug() << val;
}

void MainWindow::on_off_clicked()
{
    val = 'S';
    MainWindow::Blink(val);
    qDebug() << val;
}


void MainWindow::Blink(QString command)
{
    if(arduino->isWritable()){
        arduino->write(command.toStdString().c_str());
    }else{
        qDebug() << "Couldn't write to serial!";
    }
}
