#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import email
import imaplib

from email.utils import parseaddr
from email.header import decode_header


# ######################################################
# 接收邮件解码等模块
# ######################################################
# 自动生成文件名
def auto_file_name(file_name, local_path):
    try:
        # 分割文件名，反回其文件名和扩展名组成的元组
        name_suffix = os.path.splitext(file_name)
        num = 1
        while True:
            # 重新拼接文件名
            filename = f"{local_path}/{name_suffix[0]}({num}){name_suffix[-1]}"  # file(1).txt
            # 判断本地是否存在该文件
            isFile = os.path.isfile(filename)
            if isFile:
                num += 1
            else:
                break
        return filename
    except Exception as e:
        raise Exception(f"自动生成文件名发生异常抛出，原因：{e}")


# 缩进显示:
def parse_email(msg, indent, mail_content=""):
    if indent == 0:
        # 邮件的From, To, Subject存在于根对象上:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    # 需要解码Subject字符串:
                    value = decode_str(value)
                else:
                    # 需要解码Email地址:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            mail_content += '%s%s: %s' % ('  ' * indent, header, value) + ' '
    if msg.is_multipart():
        # 如果邮件对象是一个MIMEMultipart,
        # get_payload()返回list，包含所有的子对象:
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            # 递归打印每一个子对象:
            return parse_email(part, indent + 1, mail_content)
    else:
        # 邮件对象不是一个MIMEMultipart,
        # 就根据content_type判断:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            # 纯文本或HTML内容:
            content = msg.get_payload(decode=True)
            # 要检测文本编码:
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            mail_content += '%sText: %s' % (' ' * indent, content)
        else:
            # 不是文本，作为附件处理:
            mail_content += '%sAttachment: %s' % ('  ' * indent, content_type)
    return mail_content


# 字符编码转换
def decode_str(str_in):
    value, charset = decode_header(str_in)[0]
    if charset:
        value = value.decode(charset)
    return value


# 获得msg的编码
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            # 去掉尾部不代表编码的字段
            charset = content_type[pos + 8:].strip('; format=flowed; delsp=yes')
    return charset


# 解析邮件,获取附件
def get_att(msg, savePath):
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()

        # 如果文件名为纯数字、字母时不需要解码，否则需要解码
        try:
            fileName = decode_header(fileName)[0][0].decode(decode_header(fileName)[0][1])
        except:
            pass

        # 如果获取到了文件，则将文件保存在指定的目录下
        if fileName:
            if not os.path.exists(savePath):
                os.makedirs(savePath)
            filePath = os.path.join(savePath, fileName)
            if os.path.isfile(filePath):
                filePath = auto_file_name(fileName, savePath)
            fp = open(filePath, 'wb')
            fp.write(part.get_payload(decode=True))
            fp.close()


# ######################################################
# 接收邮件模块
# ######################################################
# 接收邮件
def get_email(json_dict):
    try:
        emailType = json_dict["emailType"]                  # 邮箱类型
        emailAddress = json_dict["emailAddress"]            # 邮箱账号
        emailPassword = json_dict["emailPassword"]          # 用户密码，授权码
        emailCount = json_dict["emailCount"]                # 邮件数量
        isReadEmail = json_dict["isReadEmail"]              # 是否仅未读邮件
        isSaveAttachment = json_dict["isSaveAttachment"]    # 是否保存附件
        savePath = json_dict["savePath"]                    # 保存目录

        smtpData = {
            "0": "imap.qq.com",  # qq邮箱
            "1": "imap.126.com",  # 126 邮箱
            "2": "imap.163.com"  # 163 邮箱
        }
        if emailType in ["0", "1", "2"]:
            mailHost = smtpData[emailType]
        else:
            raise Exception("暂时不支持该邮箱服务器，请重新选择新的邮箱服务器")

        if emailType == "2" or emailType == "1":
            imaplib.Commands['ID'] = 'AUTH'
            server = imaplib.IMAP4_SSL(mailHost)
            server.login(emailAddress, emailPassword)
            # 此处用于规避163和126获取邮件时会报错
            args = ("name", emailAddress, "contact", emailAddress, "version", "1.0.0", "vendor", "myclient")
            typ, dat = server._simple_command('ID', '("' + '" "'.join(args) + '")')
        else:
            # 连接pop服务器。如果没有使用SSL，将IMAP4_SSL()改成IMAP4()即可其他都不需要做改动
            server = imaplib.IMAP4(mailHost)
            # 登录--发送者账号和口令
            server.login(emailAddress, emailPassword)

        # 邮箱中的文件夹，默认为'INBOX'
        inbox = server.select("INBOX")

        # 是否仅未读邮件
        if isReadEmail:
            # 搜索匹配的邮件，第一个参数是字符集，None默认就是ASCII编码，第二个参数是查询条件，这里的ALL就是查找全部 UnSeen:未读邮件
            type1, emailData = server.search(None, "UnSeen")
        else:
            type1, emailData = server.search(None, "All")

        # 邮件列表,使用空格分割得到邮件索引
        msgList = emailData[0].split()

        # 邮件数量是否超出所要显示的数量
        if emailCount is None or emailCount == "":
            emailCount = 1
        else:
            if int(emailCount) >= len(msgList):
                emailCount = len(msgList)
            else:
                emailCount = int(emailCount)

        mailMessageList = []
        msgList.reverse()
        for i in range(emailCount):
            latest = msgList[i]
            # 最新邮件，第0封邮件为最早的一封邮件
            type1, datas = server.fetch(latest, '(RFC822)')
            # 使用utf-8解码
            text = datas[0][1].decode('utf8')
            # 转化为email.message对象
            message = email.message_from_string(text)
            content = parse_email(message, 0)
            mailMessageList.append(content)

            # 是否保存附件
            if isSaveAttachment:
                if savePath is None or savePath == "":
                    raise Exception ("附件保存目录为空，请检查附件保存目录是否输入正确")

                emailBody = datas[0][1]
                mail = email.message_from_bytes(emailBody)
                # 获取附件
                get_att(mail, savePath)

        # 关闭连接
        server.close()
        return mailMessageList
    except Exception as e:
        raise Exception (f'接收邮件异常抛出，原因: {e}')


if __name__ == '__main__':
    # 接收邮件
    data = {
        "emailType": "2",
        "emailAddress": "xxx@163.com",                  # 邮箱账号
        "emailPassword": "xxxx",                        # 授权码
        "emailCount": '2',                              # 邮件数量
        "isReadEmail": False,                           # 是否仅未读邮件
        "isSaveAttachment": True,                       # 是否保存附件
        "savePath": r"./附件"       					# 保存目录
    }
    mailList = get_email(data)
    print(mailList )
