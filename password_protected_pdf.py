import pikepdf


old_pdf = pikepdf.Pdf.open("protected.pdf")
no_extr= pikepdf.Permissions(extract=False)
old_pdf.save("pro_new.pdf",encryption=pikepdf.Encryption(owner="ownerpass",user="userpass",allow=no_extr))