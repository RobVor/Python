"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage."""

import num2words

#Words = [
#'One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty ','Twenty One','Twenty Two','Twenty Three','Twenty Four','Twenty Five','Twenty Six','Twenty Seven','Twenty Eight','Twenty Nine','Thirty ','Thirty One','Thirty Two','Thirty Three','Thirty Four','Thirty Five','Thirty Six','Thirty Seven','Thirty Eight','Thirty Nine','Forty ','Forty One','Forty Two','Forty Three','Forty Four','Forty Five','Forty Six','Forty Seven','Forty Eight','Forty Nine','Fifty ','Fifty One','Fifty Two','Fifty Three','Fifty Four','Fifty Five','Fifty Six','Fifty Seven','Fifty Eight','Fifty Nine','Sixty ','Sixty One','Sixty Two','Sixty Three','Sixty Four','Sixty Five','Sixty Six','Sixty Seven','Sixty Eight','Sixty Nine','Seventy ','Seventy One','Seventy Two','Seventy Three','Seventy Four','Seventy Five','Seventy Six','Seventy Seven','Seventy Eight','Seventy Nine','Eighty ','Eighty One','Eighty Two','Eighty Three','Eighty Four','Eighty Five','Eighty Six','Eighty Seven','Eighty Eight','Eighty Nine','Ninety ','Ninety One','Ninety Two','Ninety Three','Ninety Four','Ninety Five','Ninety Six','Ninety Seven','Ninety Eight','Ninety Nine','One Hundred ','One Hundred and One','One Hundred and Two','One Hundred and Three','One Hundred and Four','One Hundred and Five','One Hundred and Six','One Hundred and Seven','One Hundred and Eight','One Hundred and Nine','One Hundred and Ten','One Hundred and Eleven','One Hundred and Twelve','One Hundred and Thirteen','One Hundred and Fourteen','One Hundred and Fifteen','One Hundred and Sixteen','One Hundred and Seventeen','One Hundred and Eighteen','One Hundred and Nineteen','One Hundred and Twenty ','One Hundred and Twenty One','One Hundred and Twenty Two','One Hundred and Twenty Three','One Hundred and Twenty Four','One Hundred and Twenty Five','One Hundred and Twenty Six','One Hundred and Twenty Seven','One Hundred and Twenty Eight','One Hundred and Twenty Nine','One Hundred and Thirty ','One Hundred and Thirty One','One Hundred and Thirty Two','One Hundred and Thirty Three','One Hundred and Thirty Four','One Hundred and Thirty Five','One Hundred and Thirty Six','One Hundred and Thirty Seven','One Hundred and Thirty Eight','One Hundred and Thirty Nine','One Hundred and Forty ','One Hundred and Forty One','One Hundred and Forty Two','One Hundred and Forty Three','One Hundred and Forty Four','One Hundred and Forty Five','One Hundred and Forty Six','One Hundred and Forty Seven','One Hundred and Forty Eight','One Hundred and Forty Nine','One Hundred and Fifty ','One Hundred and Fifty One','One Hundred and Fifty Two','One Hundred and Fifty Three','One Hundred and Fifty Four','One Hundred and Fifty Five','One Hundred and Fifty Six','One Hundred and Fifty Seven','One Hundred and Fifty Eight','One Hundred and Fifty Nine','One Hundred and Sixty ','One Hundred and Sixty One','One Hundred and Sixty Two','One Hundred and Sixty Three','One Hundred and Sixty Four','One Hundred and Sixty Five','One Hundred and Sixty Six','One Hundred and Sixty Seven','One Hundred and Sixty Eight','One Hundred and Sixty Nine','One Hundred and Seventy ','One Hundred and Seventy One','One Hundred and Seventy Two','One Hundred and Seventy Three','One Hundred and Seventy Four','One Hundred and Seventy Five','One Hundred and Seventy Six','One Hundred and Seventy Seven','One Hundred and Seventy Eight','One Hundred and Seventy Nine','One Hundred and Eighty ','One Hundred and Eighty One','One Hundred and Eighty Two','One Hundred and Eighty Three','One Hundred and Eighty Four','One Hundred and Eighty Five','One Hundred and Eighty Six','One Hundred and Eighty Seven','One Hundred and Eighty Eight','One Hundred and Eighty Nine','One Hundred and Ninety ','One Hundred and Ninety One','One Hundred and Ninety Two','One Hundred and Ninety Three','One Hundred and Ninety Four','One Hundred and Ninety Five','One Hundred and Ninety Six','One Hundred and Ninety Seven','One Hundred and Ninety Eight','One Hundred and Ninety Nine','Two Hundred','Two Hundred and One','Two Hundred and Two','Two Hundred and Three','Two Hundred and Four','Two Hundred and Five','Two Hundred and Six','Two Hundred and Seven','Two Hundred and Eight','Two Hundred and Nine','Two Hundred and Ten','Two Hundred and Eleven','Two Hundred and Twelve','Two Hundred and Thirteen','Two Hundred and Fourteen','Two Hundred and Fifteen','Two Hundred and Sixteen','Two Hundred and Seventeen','Two Hundred and Eighteen','Two Hundred and Nineteen','Two Hundred and Twenty ','Two Hundred and Twenty One','Two Hundred and Twenty Two','Two Hundred and Twenty Three','Two Hundred and Twenty Four','Two Hundred and Twenty Five','Two Hundred and Twenty Six','Two Hundred and Twenty Seven','Two Hundred and Twenty Eight','Two Hundred and Twenty Nine','Two Hundred and Thirty ','Two Hundred and Thirty One','Two Hundred and Thirty Two','Two Hundred and Thirty Three','Two Hundred and Thirty Four','Two Hundred and Thirty Five','Two Hundred and Thirty Six','Two Hundred and Thirty Seven','Two Hundred and Thirty Eight','Two Hundred and Thirty Nine','Two Hundred and Forty ','Two Hundred and Forty One','Two Hundred and Forty Two','Two Hundred and Forty Three','Two Hundred and Forty Four','Two Hundred and Forty Five','Two Hundred and Forty Six','Two Hundred and Forty Seven','Two Hundred and Forty Eight','Two Hundred and Forty Nine','Two Hundred and Fifty ','Two Hundred and Fifty One','Two Hundred and Fifty Two','Two Hundred and Fifty Three','Two Hundred and Fifty Four','Two Hundred and Fifty Five','Two Hundred and Fifty Six','Two Hundred and Fifty Seven','Two Hundred and Fifty Eight','Two Hundred and Fifty Nine','Two Hundred and Sixty ','Two Hundred and Sixty One','Two Hundred and Sixty Two','Two Hundred and Sixty Three','Two Hundred and Sixty Four','Two Hundred and Sixty Five','Two Hundred and Sixty Six','Two Hundred and Sixty Seven','Two Hundred and Sixty Eight','Two Hundred and Sixty Nine','Two Hundred and Seventy ','Two Hundred and Seventy One','Two Hundred and Seventy Two','Two Hundred and Seventy Three','Two Hundred and Seventy Four','Two Hundred and Seventy Five','Two Hundred and Seventy Six','Two Hundred and Seventy Seven','Two Hundred and Seventy Eight','Two Hundred and Seventy Nine','Two Hundred and Eighty ','Two Hundred and Eighty One','Two Hundred and Eighty Two','Two Hundred and Eighty Three','Two Hundred and Eighty Four','Two Hundred and Eighty Five','Two Hundred and Eighty Six','Two Hundred and Eighty Seven','Two Hundred and Eighty Eight','Two Hundred and Eighty Nine','Two Hundred and Ninety ','Two Hundred and Ninety One','Two Hundred and Ninety Two','Two Hundred and Ninety Three','Two Hundred and Ninety Four','Two Hundred and Ninety Five','Two Hundred and Ninety Six','Two Hundred and Ninety Seven','Two Hundred and Ninety Eight','Two Hundred and Ninety Nine','Three Hundred','Three Hundred and One','Three Hundred and Two','Three Hundred and Three','Three Hundred and Four','Three Hundred and Five','Three Hundred and Six','Three Hundred and Seven','Three Hundred and Eight','Three Hundred and Nine','Three Hundred and Ten','Three Hundred and Eleven','Three Hundred and Twelve','Three Hundred and Thirteen','Three Hundred and Fourteen','Three Hundred and Fifteen','Three Hundred and Sixteen','Three Hundred and Seventeen','Three Hundred and Eighteen','Three Hundred and Nineteen','Three Hundred and Twenty ','Three Hundred and Twenty One','Three Hundred and Twenty Two','Three Hundred and Twenty Three','Three Hundred and Twenty Four','Three Hundred and Twenty Five','Three Hundred and Twenty Six','Three Hundred and Twenty Seven','Three Hundred and Twenty Eight','Three Hundred and Twenty Nine','Three Hundred and Thirty ','Three Hundred and Thirty One','Three Hundred and Thirty Two','Three Hundred and Thirty Three','Three Hundred and Thirty Four','Three Hundred and Thirty Five','Three Hundred and Thirty Six','Three Hundred and Thirty Seven','Three Hundred and Thirty Eight','Three Hundred and Thirty Nine','Three Hundred and Forty ','Three Hundred and Forty One','Three Hundred and Forty Two','Three Hundred and Forty Three','Three Hundred and Forty Four','Three Hundred and Forty Five','Three Hundred and Forty Six','Three Hundred and Forty Seven','Three Hundred and Forty Eight','Three Hundred and Forty Nine','Three Hundred and Fifty ','Three Hundred and Fifty One','Three Hundred and Fifty Two','Three Hundred and Fifty Three','Three Hundred and Fifty Four','Three Hundred and Fifty Five','Three Hundred and Fifty Six','Three Hundred and Fifty Seven','Three Hundred and Fifty Eight','Three Hundred and Fifty Nine','Three Hundred and Sixty ','Three Hundred and Sixty One','Three Hundred and Sixty Two','Three Hundred and Sixty Three','Three Hundred and Sixty Four','Three Hundred and Sixty Five','Three Hundred and Sixty Six','Three Hundred and Sixty Seven','Three Hundred and Sixty Eight','Three Hundred and Sixty Nine','Three Hundred and Seventy ','Three Hundred and Seventy One','Three Hundred and Seventy Two','Three Hundred and Seventy Three','Three Hundred and Seventy Four','Three Hundred and Seventy Five','Three Hundred and Seventy Six','Three Hundred and Seventy Seven','Three Hundred and Seventy Eight','Three Hundred and Seventy Nine','Three Hundred and Eighty ','Three Hundred and Eighty One','Three Hundred and Eighty Two','Three Hundred and Eighty Three','Three Hundred and Eighty Four','Three Hundred and Eighty Five','Three Hundred and Eighty Six','Three Hundred and Eighty Seven','Three Hundred and Eighty Eight','Three Hundred and Eighty Nine','Three Hundred and Ninety ','Three Hundred and Ninety One','Three Hundred and Ninety Two','Three Hundred and Ninety Three','Three Hundred and Ninety Four','Three Hundred and Ninety Five','Three Hundred and Ninety Six','Three Hundred and Ninety Seven','Three Hundred and Ninety Eight','Three Hundred and Ninety Nine','Four Hundred','Four Hundred and One','Four Hundred and Two','Four Hundred and Three','Four Hundred and Four','Four Hundred and Five','Four Hundred and Six','Four Hundred and Seven','Four Hundred and Eight','Four Hundred and Nine','Four Hundred and Ten','Four Hundred and Eleven','Four Hundred and Twelve','Four Hundred and Thirteen','Four Hundred and Fourteen','Four Hundred and Fifteen','Four Hundred and Sixteen','Four Hundred and Seventeen','Four Hundred and Eighteen','Four Hundred and Nineteen','Four Hundred and Twenty ','Four Hundred and Twenty One','Four Hundred and Twenty Two','Four Hundred and Twenty Three','Four Hundred and Twenty Four','Four Hundred and Twenty Five','Four Hundred and Twenty Six','Four Hundred and Twenty Seven','Four Hundred and Twenty Eight','Four Hundred and Twenty Nine','Four Hundred and Thirty ','Four Hundred and Thirty One','Four Hundred and Thirty Two','Four Hundred and Thirty Three','Four Hundred and Thirty Four','Four Hundred and Thirty Five','Four Hundred and Thirty Six','Four Hundred and Thirty Seven','Four Hundred and Thirty Eight','Four Hundred and Thirty Nine','Four Hundred and Forty ','Four Hundred and Forty One','Four Hundred and Forty Two','Four Hundred and Forty Three','Four Hundred and Forty Four','Four Hundred and Forty Five','Four Hundred and Forty Six','Four Hundred and Forty Seven','Four Hundred and Forty Eight','Four Hundred and Forty Nine','Four Hundred and Fifty ','Four Hundred and Fifty One','Four Hundred and Fifty Two','Four Hundred and Fifty Three','Four Hundred and Fifty Four','Four Hundred and Fifty Five','Four Hundred and Fifty Six','Four Hundred and Fifty Seven','Four Hundred and Fifty Eight','Four Hundred and Fifty Nine','Four Hundred and Sixty ','Four Hundred and Sixty One','Four Hundred and Sixty Two','Four Hundred and Sixty Three','Four Hundred and Sixty Four','Four Hundred and Sixty Five','Four Hundred and Sixty Six','Four Hundred and Sixty Seven','Four Hundred and Sixty Eight','Four Hundred and Sixty Nine','Four Hundred and Seventy ','Four Hundred and Seventy One','Four Hundred and Seventy Two','Four Hundred and Seventy Three','Four Hundred and Seventy Four','Four Hundred and Seventy Five','Four Hundred and Seventy Six','Four Hundred and Seventy Seven','Four Hundred and Seventy Eight','Four Hundred and Seventy Nine','Four Hundred and Eighty ','Four Hundred and Eighty One','Four Hundred and Eighty Two','Four Hundred and Eighty Three','Four Hundred and Eighty Four','Four Hundred and Eighty Five','Four Hundred and Eighty Six','Four Hundred and Eighty Seven','Four Hundred and Eighty Eight','Four Hundred and Eighty Nine','Four Hundred and Ninety ','Four Hundred and Ninety One','Four Hundred and Ninety Two','Four Hundred and Ninety Three','Four Hundred and Ninety Four','Four Hundred and Ninety Five','Four Hundred and Ninety Six','Four Hundred and Ninety Seven','Four Hundred and Ninety Eight','Four Hundred and Ninety Nine','Five Hundred','Five Hundred and One','Five Hundred and Two','Five Hundred and Three','Five Hundred and Four','Five Hundred and Five','Five Hundred and Six','Five Hundred and Seven','Five Hundred and Eight','Five Hundred and Nine','Five Hundred and Ten','Five Hundred and Eleven','Five Hundred and Twelve','Five Hundred and Thirteen','Five Hundred and Fourteen','Five Hundred and Fifteen','Five Hundred and Sixteen','Five Hundred and Seventeen','Five Hundred and Eighteen','Five Hundred and Nineteen','Five Hundred and Twenty ','Five Hundred and Twenty One','Five Hundred and Twenty Two','Five Hundred and Twenty Three','Five Hundred and Twenty Four','Five Hundred and Twenty Five','Five Hundred and Twenty Six','Five Hundred and Twenty Seven','Five Hundred and Twenty Eight','Five Hundred and Twenty Nine','Five Hundred and Thirty ','Five Hundred and Thirty One','Five Hundred and Thirty Two','Five Hundred and Thirty Three','Five Hundred and Thirty Four','Five Hundred and Thirty Five','Five Hundred and Thirty Six','Five Hundred and Thirty Seven','Five Hundred and Thirty Eight','Five Hundred and Thirty Nine','Five Hundred and Forty ','Five Hundred and Forty One','Five Hundred and Forty Two','Five Hundred and Forty Three','Five Hundred and Forty Four','Five Hundred and Forty Five','Five Hundred and Forty Six','Five Hundred and Forty Seven','Five Hundred and Forty Eight','Five Hundred and Forty Nine','Five Hundred and Fifty ','Five Hundred and Fifty One','Five Hundred and Fifty Two','Five Hundred and Fifty Three','Five Hundred and Fifty Four','Five Hundred and Fifty Five','Five Hundred and Fifty Six','Five Hundred and Fifty Seven','Five Hundred and Fifty Eight','Five Hundred and Fifty Nine','Five Hundred and Sixty ','Five Hundred and Sixty One','Five Hundred and Sixty Two','Five Hundred and Sixty Three','Five Hundred and Sixty Four','Five Hundred and Sixty Five','Five Hundred and Sixty Six','Five Hundred and Sixty Seven','Five Hundred and Sixty Eight','Five Hundred and Sixty Nine','Five Hundred and Seventy ','Five Hundred and Seventy One','Five Hundred and Seventy Two','Five Hundred and Seventy Three','Five Hundred and Seventy Four','Five Hundred and Seventy Five','Five Hundred and Seventy Six','Five Hundred and Seventy Seven','Five Hundred and Seventy Eight','Five Hundred and Seventy Nine','Five Hundred and Eighty ','Five Hundred and Eighty One','Five Hundred and Eighty Two','Five Hundred and Eighty Three','Five Hundred and Eighty Four','Five Hundred and Eighty Five','Five Hundred and Eighty Six','Five Hundred and Eighty Seven','Five Hundred and Eighty Eight','Five Hundred and Eighty Nine','Five Hundred and Ninety ','Five Hundred and Ninety One','Five Hundred and Ninety Two','Five Hundred and Ninety Three','Five Hundred and Ninety Four','Five Hundred and Ninety Five','Five Hundred and Ninety Six','Five Hundred and Ninety Seven','Five Hundred and Ninety Eight','Five Hundred and Ninety Nine','Six Hundred','Six Hundred and One','Six Hundred and Two','Six Hundred and Three','Six Hundred and Four','Six Hundred and Five','Six Hundred and Six','Six Hundred and Seven','Six Hundred and Eight','Six Hundred and Nine','Six Hundred and Ten','Six Hundred and Eleven','Six Hundred and Twelve','Six Hundred and Thirteen','Six Hundred and Fourteen','Six Hundred and Fifteen','Six Hundred and Sixteen','Six Hundred and Seventeen','Six Hundred and Eighteen','Six Hundred and Nineteen','Six Hundred and Twenty ','Six Hundred and Twenty One','Six Hundred and Twenty Two','Six Hundred and Twenty Three','Six Hundred and Twenty Four','Six Hundred and Twenty Five','Six Hundred and Twenty Six','Six Hundred and Twenty Seven','Six Hundred and Twenty Eight','Six Hundred and Twenty Nine','Six Hundred and Thirty ','Six Hundred and Thirty One','Six Hundred and Thirty Two','Six Hundred and Thirty Three','Six Hundred and Thirty Four','Six Hundred and Thirty Five','Six Hundred and Thirty Six','Six Hundred and Thirty Seven','Six Hundred and Thirty Eight','Six Hundred and Thirty Nine','Six Hundred and Forty ','Six Hundred and Forty One','Six Hundred and Forty Two','Six Hundred and Forty Three','Six Hundred and Forty Four','Six Hundred and Forty Five','Six Hundred and Forty Six','Six Hundred and Forty Seven','Six Hundred and Forty Eight','Six Hundred and Forty Nine','Six Hundred and Fifty ','Six Hundred and Fifty One','Six Hundred and Fifty Two','Six Hundred and Fifty Three','Six Hundred and Fifty Four','Six Hundred and Fifty Five','Six Hundred and Fifty Six','Six Hundred and Fifty Seven','Six Hundred and Fifty Eight','Six Hundred and Fifty Nine','Six Hundred and Sixty ','Six Hundred and Sixty One','Six Hundred and Sixty Two','Six Hundred and Sixty Three','Six Hundred and Sixty Four','Six Hundred and Sixty Five','Six Hundred and Sixty Six','Six Hundred and Sixty Seven','Six Hundred and Sixty Eight','Six Hundred and Sixty Nine','Six Hundred and Seventy ','Six Hundred and Seventy One','Six Hundred and Seventy Two','Six Hundred and Seventy Three','Six Hundred and Seventy Four','Six Hundred and Seventy Five','Six Hundred and Seventy Six','Six Hundred and Seventy Seven','Six Hundred and Seventy Eight','Six Hundred and Seventy Nine','Six Hundred and Eighty ','Six Hundred and Eighty One','Six Hundred and Eighty Two','Six Hundred and Eighty Three','Six Hundred and Eighty Four','Six Hundred and Eighty Five','Six Hundred and Eighty Six','Six Hundred and Eighty Seven','Six Hundred and Eighty Eight','Six Hundred and Eighty Nine','Six Hundred and Ninety ','Six Hundred and Ninety One','Six Hundred and Ninety Two','Six Hundred and Ninety Three','Six Hundred and Ninety Four','Six Hundred and Ninety Five','Six Hundred and Ninety Six','Six Hundred and Ninety Seven','Six Hundred and Ninety Eight','Six Hundred and Ninety Nine','Seven Hundred','Seven Hundred and One','Seven Hundred and Two','Seven Hundred and Three','Seven Hundred and Four','Seven Hundred and Five','Seven Hundred and Six','Seven Hundred and Seven','Seven Hundred and Eight','Seven Hundred and Nine','Seven Hundred and Ten','Seven Hundred and Eleven','Seven Hundred and Twelve','Seven Hundred and Thirteen','Seven Hundred and Fourteen','Seven Hundred and Fifteen','Seven Hundred and Sixteen','Seven Hundred and Seventeen','Seven Hundred and Eighteen','Seven Hundred and Nineteen','Seven Hundred and Twenty ','Seven Hundred and Twenty One','Seven Hundred and Twenty Two','Seven Hundred and Twenty Three','Seven Hundred and Twenty Four','Seven Hundred and Twenty Five','Seven Hundred and Twenty Six','Seven Hundred and Twenty Seven','Seven Hundred and Twenty Eight','Seven Hundred and Twenty Nine','Seven Hundred and Thirty ','Seven Hundred and Thirty One','Seven Hundred and Thirty Two','Seven Hundred and Thirty Three','Seven Hundred and Thirty Four','Seven Hundred and Thirty Five','Seven Hundred and Thirty Six','Seven Hundred and Thirty Seven','Seven Hundred and Thirty Eight','Seven Hundred and Thirty Nine','Seven Hundred and Forty ','Seven Hundred and Forty One','Seven Hundred and Forty Two','Seven Hundred and Forty Three','Seven Hundred and Forty Four','Seven Hundred and Forty Five','Seven Hundred and Forty Six','Seven Hundred and Forty Seven','Seven Hundred and Forty Eight','Seven Hundred and Forty Nine','Seven Hundred and Fifty ','Seven Hundred and Fifty One','Seven Hundred and Fifty Two','Seven Hundred and Fifty Three','Seven Hundred and Fifty Four','Seven Hundred and Fifty Five','Seven Hundred and Fifty Six','Seven Hundred and Fifty Seven','Seven Hundred and Fifty Eight','Seven Hundred and Fifty Nine','Seven Hundred and Sixty ','Seven Hundred and Sixty One','Seven Hundred and Sixty Two','Seven Hundred and Sixty Three','Seven Hundred and Sixty Four','Seven Hundred and Sixty Five','Seven Hundred and Sixty Six','Seven Hundred and Sixty Seven','Seven Hundred and Sixty Eight','Seven Hundred and Sixty Nine','Seven Hundred and Seventy ','Seven Hundred and Seventy One','Seven Hundred and Seventy Two','Seven Hundred and Seventy Three','Seven Hundred and Seventy Four','Seven Hundred and Seventy Five','Seven Hundred and Seventy Six','Seven Hundred and Seventy Seven','Seven Hundred and Seventy Eight','Seven Hundred and Seventy Nine','Seven Hundred and Eighty ','Seven Hundred and Eighty One','Seven Hundred and Eighty Two','Seven Hundred and Eighty Three','Seven Hundred and Eighty Four','Seven Hundred and Eighty Five','Seven Hundred and Eighty Six','Seven Hundred and Eighty Seven','Seven Hundred and Eighty Eight','Seven Hundred and Eighty Nine','Seven Hundred and Ninety ','Seven Hundred and Ninety One','Seven Hundred and Ninety Two','Seven Hundred and Ninety Three','Seven Hundred and Ninety Four','Seven Hundred and Ninety Five','Seven Hundred and Ninety Six','Seven Hundred and Ninety Seven','Seven Hundred and Ninety Eight','Seven Hundred and Ninety Nine','Eight Hundred','Eight Hundred and One','Eight Hundred and Two','Eight Hundred and Three','Eight Hundred and Four','Eight Hundred and Five','Eight Hundred and Six','Eight Hundred and Seven','Eight Hundred and Eight','Eight Hundred and Nine','Eight Hundred and Ten','Eight Hundred and Eleven','Eight Hundred and Twelve','Eight Hundred and Thirteen','Eight Hundred and Fourteen','Eight Hundred and Fifteen','Eight Hundred and Sixteen','Eight Hundred and Seventeen','Eight Hundred and Eighteen','Eight Hundred and Nineteen','Eight Hundred and Twenty ','Eight Hundred and Twenty One','Eight Hundred and Twenty Two','Eight Hundred and Twenty Three','Eight Hundred and Twenty Four','Eight Hundred and Twenty Five','Eight Hundred and Twenty Six','Eight Hundred and Twenty Seven','Eight Hundred and Twenty Eight','Eight Hundred and Twenty Nine','Eight Hundred and Thirty ','Eight Hundred and Thirty One','Eight Hundred and Thirty Two','Eight Hundred and Thirty Three','Eight Hundred and Thirty Four','Eight Hundred and Thirty Five','Eight Hundred and Thirty Six','Eight Hundred and Thirty Seven','Eight Hundred and Thirty Eight','Eight Hundred and Thirty Nine','Eight Hundred and Forty ','Eight Hundred and Forty One','Eight Hundred and Forty Two','Eight Hundred and Forty Three','Eight Hundred and Forty Four','Eight Hundred and Forty Five','Eight Hundred and Forty Six','Eight Hundred and Forty Seven','Eight Hundred and Forty Eight','Eight Hundred and Forty Nine','Eight Hundred and Fifty ','Eight Hundred and Fifty One','Eight Hundred and Fifty Two','Eight Hundred and Fifty Three','Eight Hundred and Fifty Four','Eight Hundred and Fifty Five','Eight Hundred and Fifty Six','Eight Hundred and Fifty Seven','Eight Hundred and Fifty Eight','Eight Hundred and Fifty Nine','Eight Hundred and Sixty ','Eight Hundred and Sixty One','Eight Hundred and Sixty Two','Eight Hundred and Sixty Three','Eight Hundred and Sixty Four','Eight Hundred and Sixty Five','Eight Hundred and Sixty Six','Eight Hundred and Sixty Seven','Eight Hundred and Sixty Eight','Eight Hundred and Sixty Nine','Eight Hundred and Seventy ','Eight Hundred and Seventy One','Eight Hundred and Seventy Two','Eight Hundred and Seventy Three','Eight Hundred and Seventy Four','Eight Hundred and Seventy Five','Eight Hundred and Seventy Six','Eight Hundred and Seventy Seven','Eight Hundred and Seventy Eight','Eight Hundred and Seventy Nine','Eight Hundred and Eighty ','Eight Hundred and Eighty One','Eight Hundred and Eighty Two','Eight Hundred and Eighty Three','Eight Hundred and Eighty Four','Eight Hundred and Eighty Five','Eight Hundred and Eighty Six','Eight Hundred and Eighty Seven','Eight Hundred and Eighty Eight','Eight Hundred and Eighty Nine','Eight Hundred and Ninety ','Eight Hundred and Ninety One','Eight Hundred and Ninety Two','Eight Hundred and Ninety Three','Eight Hundred and Ninety Four','Eight Hundred and Ninety Five','Eight Hundred and Ninety Six','Eight Hundred and Ninety Seven','Eight Hundred and Ninety Eight','Eight Hundred and Ninety Nine','Nine Hundred','Nine Hundred and One','Nine Hundred and Two','Nine Hundred and Three','Nine Hundred and Four','Nine Hundred and Five','Nine Hundred and Six','Nine Hundred and Seven','Nine Hundred and Eight','Nine Hundred and Nine','Nine Hundred and Ten','Nine Hundred and Eleven','Nine Hundred and Twelve','Nine Hundred and Thirteen','Nine Hundred and Fourteen','Nine Hundred and Fifteen','Nine Hundred and Sixteen','Nine Hundred and Seventeen','Nine Hundred and Eighteen','Nine Hundred and Nineteen','Nine Hundred and Twenty ','Nine Hundred and Twenty One','Nine Hundred and Twenty Two','Nine Hundred and Twenty Three','Nine Hundred and Twenty Four','Nine Hundred and Twenty Five','Nine Hundred and Twenty Six','Nine Hundred and Twenty Seven','Nine Hundred and Twenty Eight','Nine Hundred and Twenty Nine','Nine Hundred and Thirty ','Nine Hundred and Thirty One','Nine Hundred and Thirty Two','Nine Hundred and Thirty Three','Nine Hundred and Thirty Four','Nine Hundred and Thirty Five','Nine Hundred and Thirty Six','Nine Hundred and Thirty Seven','Nine Hundred and Thirty Eight','Nine Hundred and Thirty Nine','Nine Hundred and Forty ','Nine Hundred and Forty One','Nine Hundred and Forty Two','Nine Hundred and Forty Three','Nine Hundred and Forty Four','Nine Hundred and Forty Five','Nine Hundred and Forty Six','Nine Hundred and Forty Seven','Nine Hundred and Forty Eight','Nine Hundred and Forty Nine','Nine Hundred and Fifty ','Nine Hundred and Fifty One','Nine Hundred and Fifty Two','Nine Hundred and Fifty Three','Nine Hundred and Fifty Four','Nine Hundred and Fifty Five','Nine Hundred and Fifty Six','Nine Hundred and Fifty Seven','Nine Hundred and Fifty Eight','Nine Hundred and Fifty Nine','Nine Hundred and Sixty ','Nine Hundred and Sixty One','Nine Hundred and Sixty Two','Nine Hundred and Sixty Three','Nine Hundred and Sixty Four','Nine Hundred and Sixty Five','Nine Hundred and Sixty Six','Nine Hundred and Sixty Seven','Nine Hundred and Sixty Eight','Nine Hundred and Sixty Nine','Nine Hundred and Seventy ','Nine Hundred and Seventy One','Nine Hundred and Seventy Two','Nine Hundred and Seventy Three','Nine Hundred and Seventy Four','Nine Hundred and Seventy Five','Nine Hundred and Seventy Six','Nine Hundred and Seventy Seven','Nine Hundred and Seventy Eight','Nine Hundred and Seventy Nine','Nine Hundred and Eighty ','Nine Hundred and Eighty One','Nine Hundred and Eighty Two','Nine Hundred and Eighty Three','Nine Hundred and Eighty Four','Nine Hundred and Eighty Five','Nine Hundred and Eighty Six','Nine Hundred and Eighty Seven','Nine Hundred and Eighty Eight','Nine Hundred and Eighty Nine','Nine Hundred and Ninety ','Nine Hundred and Ninety One','Nine Hundred and Ninety Two','Nine Hundred and Ninety Three','Nine Hundred and Ninety Four','Nine Hundred and Ninety Five','Nine Hundred and Ninety Six','Nine Hundred and Ninety Seven','Nine Hundred and Ninety Eight','Nine Hundred and Ninety Nine','One Thousand'
#]

Words = []
Result = 0

for num in range(1, 1001):
    Words.append(num2words.num2words(num))

for i in Words:
    i = i.replace(" ","")
    i = i.replace("-","")
    for j in i:
        Result += len(j)

print(Words)
print(Result)