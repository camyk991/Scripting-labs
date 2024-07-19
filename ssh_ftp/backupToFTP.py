import os
import tarfile
from ftplib import FTP
from datetime import datetime

SOURCE_DIR = 'tobackup' 
BACKUP_DIR = 'backup' 
FTP_SERVER = '10.0.2.15'
FTP_USER = 'kamykftp'
FTP_PASSWORD = 'cisco'
FTP_TARGET_DIR = './'

def create_backup_archive(source_dir, backup_dir):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = os.path.join(backup_dir, f'backup_{timestamp}.tar.gz')
    
    with tarfile.open(archive_name, 'w:gz') as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
    
    return archive_name

def upload_to_ftp(file_path, ftp_server, ftp_user, ftp_password, ftp_target_dir):
    with FTP(ftp_server) as ftp:
        ftp.login(ftp_user, ftp_password)
        ftp.cwd(ftp_target_dir)
        
        with open(file_path, 'rb') as f:
            ftp.storbinary(f'STOR {os.path.basename(file_path)}', f)

def clean_up_local_backup(file_path):
    os.remove(file_path)

if __name__ == '__main__':
    os.makedirs(BACKUP_DIR, exist_ok=True)
    
    backup_archive = create_backup_archive(SOURCE_DIR, BACKUP_DIR)
    
    try:
        upload_to_ftp(backup_archive, FTP_SERVER, FTP_USER, FTP_PASSWORD, FTP_TARGET_DIR)
        print(f'Pomyślnie przesłano kopię zapasową na serwer FTP')
    except Exception as e:
        print(e)

    
    clean_up_local_backup(backup_archive)



