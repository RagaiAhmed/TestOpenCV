#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QtSerialPort/QSerialPort>
#include <QtSerialPort/QSerialPortInfo>
#include <QDebug>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_redbutton_pressed();

    void on_bluebutton_pressed();

    void Blink(QString);

    void on_off_clicked();

    void on_Blink_all_clicked();

private:
    Ui::MainWindow *ui;
    QSerialPort *arduino;
    static const quint16 arduino_uno_vendor_id = 2341;
    static const quint16 arduino_uno_product_id = 43;
    QString arduino_port_name;
    bool arduino_is_available;
    QString val;

};
#endif // MAINWINDOW_H
