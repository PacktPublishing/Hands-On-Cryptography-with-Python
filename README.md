## $5 Tech Unlocked 2021!
[Buy and download this Book for only $5 on PacktPub.com](https://www.packtpub.com/product/hands-on-cryptography-with-python/9781789534443)
-----
*If you have read this book, please leave a review on [Amazon.com](https://www.amazon.com/gp/product/1789534445).     Potential readers can then use your unbiased opinion to help them make purchase decisions. Thank you. The $5 campaign         runs from __December 15th 2020__ to __January 13th 2021.__*

# Hands-On Cryptography with Python

<a href="https://www.packtpub.com/networking-and-servers/hands-cryptography-python?utm_source=repository&utm_medium=github&utm_campaign=repository&utm_term=9781789534443"><img src="https://d255esdrn735hr.cloudfront.net/sites/default/files/imagecache/ppv4_main_book_cover/B11735.png" alt="Hands-On Cryptography with Python" height="256px" align="right"></a>

This is the code repository for [Hands-On Cryptography with Python](https://www.packtpub.com/networking-and-servers/hands-cryptography-python), published by Packt.

**Leverage the power of Python to encrypt and decrypt data**

## What is this book about?
Cryptography is essential for protecting sensitive information, but it is often performed inadequately or incorrectly.

This book covers the following exciting features:
* Protect data with encryption and hashing
* Explore and compare various encryption methods
* Encrypt data using the Caesar Cipher technique
* Make hashes and crack them
* Learn how to use three NIST-recommended systems: AES, SHA, and RSA

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1789534445) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>


## Instructions and Navigations
All of the code is organized into folders. For example, Chapter01.

The code will look like the following:
```
 alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 str_in = raw_input("Enter message, like HELLO: ")

 n = len(str_in)
 str_out = ""

 for i in range(n):
    c = str_in[i]
    loc = alpha.find(c)
    print i, c, loc, 
    newloc = loc + 3
    str_out += alpha[newloc]
    print newloc, str_out

 print "Obfuscated version:", str_out
```

**Following is what you need for this book:**
Hands-On Cryptography with Python is for security professionals who want to learn to encrypt and evaluate data, and compare different encryption methods.

With the following software and hardware list you can run all code files present in the book (Chapter 1-3).

### Software and Hardware List

| Chapter  | Software required                   | OS required                        |
| -------- | ------------------------------------| -----------------------------------|
| 1-3      | Python (latest version)             | macOS or Ubuntu/Linux              |


We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://www.packtpub.com/sites/default/files/downloads/HandsOnCryptographywithPython_ColorImages.pdf).

### Related products <Paste books from the Other books you may enjoy section>
* Python Penetration Testing Cookbook [[Packt]](https://www.packtpub.com/networking-and-servers/python-penetration-testing-cookbook?utm_source=repository&utm_medium=github&utm_campaign=repository&utm_term=9781784399771) [[Amazon]](https://www.amazon.com/dp/1784399779)

* Python For Offensive PenTest [[Packt]](https://www.packtpub.com/networking-and-servers/python-offensive-pentest?utm_source=repository&utm_medium=github&utm_campaign=repository&utm_term=9781788838979) [[Amazon]](https://www.amazon.com/dp/1788838971)

## Get to Know the Author
**Sam Bowne**
has been teaching computer networking and security classes at City College of San Francisco since 2000. He has given talks and hands-on training at DEFCON, HOPE, B-Sides SF, B-Sides LV, BayThreat, LayerOne, Toorcon, and many other schools and conferences. He has done his PhD and CISSP. He is a DEF CON Black-Badge co-winner.

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSdy7dATC6QmEL81FIUuymZ0Wy9vH1jHkvpY57OiMeKGqib_Ow/viewform) if you have any feedback or suggestions.

