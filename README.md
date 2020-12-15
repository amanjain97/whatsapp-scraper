# Whatsapp-scraper

## Usage
1. Add contacts in contacts.csv in same folder
2. Run below command for sending image
```python
python3 whatsapp_scraper.py --chrome_driver chromedriver --message hi --file_type image --file_path media/myimage.png
```
3. Run below command for sending document
```python
python3 whatsapp_scraper.py --chrome_driver chromedriver --message hi --file_type document --file_path media/file.pdf
```
4. Run below command for sending message only
```python
python3 whatsapp_scraper.py --chrome_driver chromedriver --message hi --file_type na
```
