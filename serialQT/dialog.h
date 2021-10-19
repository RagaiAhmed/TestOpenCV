#ifndef DIALOG_H
#define DIALOG_H
#include <QSerialPort>
#include <QDialog>

QT_BEGIN_NAMESPACE
namespace Ui { class Dialog; }
QT_END_NAMESPACE

class Dialog : public QDialog
{
    Q_OBJECT

public:
    Dialog(QWidget *parent = nullptr);
    ~Dialog();

private slots:
    void on_pushButton_clicked();

    void on_pushButton_2_clicked();
    void sendMESSAGE(QString result);

private:
    Ui::Dialog *ui;
    QSerialPort *arduino;
    static const quint16 arduino_uno_vendor_id= 2341;
    static const quint16 arduino_uno_product_id= 0043;
    QString  arduino_port_name;
    bool arduino_is_available;

};
#endif // DIALOG_H
