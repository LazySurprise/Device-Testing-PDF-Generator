# MULTI PAGE PDF
import datetime
import os
import io
from os.path import join as pjoin
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def write_on_pdf(property_name, property_info, istc_info,
                 system_description, circuit_pathways,
                 alarm_devices):
    # READ ENTIRE PDF
    pdf_reader = PdfFileReader(open('test_form.pdf', 'rb'))
    # GET NUMBER OF PAGES
    num_pages = pdf_reader.getNumPages()
    # CREATE PDF WRITER
    output = PdfFileWriter()

    # LOOP THROUGH ALL PAGES
    for page in range(0, num_pages):

        # CHECK FOR PAGE
        if page == 0:

            # CREATE READABLE STREAM FROM BYTES LIKE OBJECT
            packet = io.BytesIO()
            
            # Create NEW PAGE
            can = canvas.Canvas(packet, pagesize=letter)

            # WRITE ON PAGE
            can.drawString(325, 605, 'property_name')
            can.drawString(308, 588, 'property_address')
            can.drawString(325, 572, 'property_description')
            can.drawString(296, 555, 'occupancy_type')
            can.drawString(302, 537, 'rep_name')
            can.drawString(300, 521, 'rep_address')
            can.drawString(137, 505, 'rep_phone')
            can.drawString(265, 505, 'rep_fax')
            can.drawString(410, 505, 'rep_email') 
            can.drawString(300, 487, 'authority_jurisdiction')
            can.drawString(137, 470, 'aj_phone')

            # second part of form
    
        ##    can.drawString(301, 418, release_to) 
        ##    can.drawString(286, 402, address)
        ##    can.drawString(305, 385, phone_number)
        ##    can.drawString(137, 368, phone_number) 
        ##    can.drawString(265, 368, phone_number)
        ##    can.drawString(410, 368, address)
        ##    can.drawString(301, 351, release_to) 
        ##    can.drawString(301, 335, release_to)
        ##    can.drawString(303, 317, phone_number)
        ##    can.drawString(137, 300, phone_number) 
        ##    can.drawString(265, 300, phone_number)
        ##    can.drawString(410, 300, address)
        ##    can.drawString(430, 284, patient_dob)
        ##    can.drawString(303, 267, release_to) 
        ##    can.drawString(303, 250, release_to)
        ##    can.drawString(137, 233, phone_number)
        ##    can.drawString(265, 233, phone_number) 
        ##    can.drawString(410, 233, release_to)
        ##    can.drawString(155, 216, patient_dob)
        ##    can.drawString(283, 216, phone_number) 
        ##    can.drawString(485, 216, patient_dob)

            '''    # checked or not
            checked = 'X'
            not_checked = ''
            x = 0
            while x < len(check_list):
                if check_list[x] == True:
                    print(check_list[x])
                    check_list[x] = checked
                else:
                    check_list[x] = not_checked
                x += 1

            # third part of form
            can.drawString(88, 164, check_list[0])
            can.drawString(88, 148, check_list[1]) 
            can.drawString(88, 132, check_list[2])
            can.drawString(88, 116, check_list[3])
            can.drawString(88, 83, check_list[4]) 
            can.drawString(98, 99, check_list[5])
            can.drawString(171, 99, check_list[6])
            can.drawString(237, 99, check_list[7]) 
            can.drawString(292, 99, check_list[8])'''

            # SAVE OUR INPUT FOR PDF
            can.save()

            # USE BEGINNING OF FILE AS REFERENCE POSITION
            packet.seek(0)
            # READ PACKET AND GET INPUT
            report_pdf = PdfFileReader(packet)
            
            # GET OG PDF PAGE
            page_merge_1 = pdf_reader.getPage(0)
            # MERGE OG PAGE WITH INPUT
            page_merge_1.mergePage(report_pdf.getPage(0))
            # LAYOUT OG PAGE
            output.addPage(page_merge_1)
            
            
        # CHECK FOR PAGE
        elif page == 1:

            # CREATE READABLE STREAM FROM BYTES LIKE OBJECT
            packet = io.BytesIO()

            # INPUT FOR PAGE 2
            can1 = canvas.Canvas(packet, pagesize=letter)

            can1.drawString(170, 690, 'property_name')
            can1.drawString(430, 690, 'property_address')
            can1.drawString(255, 653, 'property_description')
            can1.drawString(492, 653, 'occupancy_type')
            can1.drawString(376, 632, 'X')
            can1.drawString(87, 596, 'X')
            can1.drawString(87, 579, 'X')
            can1.drawString(231, 579, 'X')
            can1.drawString(318, 579, 'X')
            can1.drawString(87, 563, 'X')
            can1.drawString(305, 563, 'rep_email')
            can1.drawString(87, 527, 'X')
            can1.drawString(231, 527, 'X')
            can1.drawString(376, 527, 'X')
            can1.drawString(87, 500, 'X')
            can1.drawString(231, 500, 'X')
            can1.drawString(376, 500, 'X')
            can1.drawString(87, 484, 'X')
            can1.drawString(333, 484, 'X')
            can1.drawString(87, 467, 'X')
            can1.drawString(305, 468, 'property_address')
            can1.drawString(87, 431, 'X')
            can1.drawString(387, 415, 'property_address')
            can1.drawString(318, 395, 'X')
            can1.drawString(400, 379, 'aj_fax')
            can1.drawString(250, 363, 'aj_email')
            can1.drawString(460, 363, 'aj_email')
            ########
            can1.drawString(87, 345, 'X')
            can1.drawString(387, 345, 'property_address')
            can1.drawString(333, 325, 'X')
            can1.drawString(250, 291, 'property_address')
            can1.drawString(460, 291, 'property_address')
            can1.drawString(250, 272, 'property_address')
            can1.drawString(460, 272, 'property_address')
            can1.drawString(250, 256, 'property_address')
            can1.drawString(460, 256, 'property_address')
            can1.drawString(300, 240, 'property_address')
            can1.drawString(460, 240, 'aj_fax')
            can1.drawString(300, 223, 'property_address')
            ########
            can1.drawString(300, 185, 'property_address')
            can1.drawString(303, 167, 'X')
            can1.drawString(375, 167, 'X')
            can1.drawString(433, 167, 'X')
            can1.drawString(490, 167, 'X')

            # SAVE PAGE 2 INPUT
            can1.save()

            # USE BEGINNING OF FILE AS PAGE REFERENCE
            packet.seek(0)
            # READ PACKET AND GET INPUT
            report_pdf = PdfFileReader(packet)

            # GET OG PAGE TO MERGE
            page_merge_2 = pdf_reader.getPage(1)
            # MERGE OG PAGE AND INPUT
            page_merge_2.mergePage(report_pdf.getPage(0))
            # ADD PAGE TO PDF
            output.addPage(page_merge_2)

        elif page == 2:

            # CREATE READABLE STREAM FROM BYTES LIKE OBJECT
            packet = io.BytesIO()

            # INPUT FOR PAGE 2
            can2 = canvas.Canvas(packet, pagesize=letter)

            can2.drawString(168, 655, 'property_name')
            can2.drawString(330, 655, 'property_address')
            can2.drawString(483, 655, 'property_description')
            can2.drawString(168, 608, 'occupancy_type')
            can2.drawString(376, 608, 'property_address')
            can2.drawString(87, 572, 'X')
            can2.drawString(87, 555, 'X')
            can2.drawString(87, 539, 'X')
            can2.drawString(318, 504, 'property_address')
            can2.drawString(168, 448, 'property_name')
            can2.drawString(330, 448, 'property_address')
            can2.drawString(483, 448, 'property_description')
            can2.drawString(168, 402, 'property_name')
            can2.drawString(376, 402, 'property_address')
            can2.drawString(87, 365, 'X')
            can2.drawString(87, 349, 'X')
            can2.drawString(87, 332, 'X')
            can2.drawString(168, 278, 'property_address')
            can2.drawString(330, 278, 'property_address')
            can2.drawString(483, 278, 'property_address')
            can2.drawString(168, 231, 'property_address')
            can2.drawString(376, 231, 'property_address')
            can2.drawString(87, 195, 'X')
            can2.drawString(87, 179, 'X')
            can2.drawString(87, 162, 'X')

            # SAVE PAGE 2 INPUT
            can2.save()

            # USE BEGINNING OF FILE AS PAGE REFERENCE
            packet.seek(0)
            # READ PACKET AND GET INPUT
            report_pdf = PdfFileReader(packet)

            # GET OG PAGE TO MERGE
            page_merge_3 = pdf_reader.getPage(2)
            # MERGE OG PAGE AND INPUT
            page_merge_3.mergePage(report_pdf.getPage(0))
            # ADD PAGE TO PDF
            output.addPage(page_merge_3)

        elif page == 3:

            # CREATE READABLE STREAM FROM BYTES LIKE OBJECT
            packet = io.BytesIO()

            # INPUT FOR PAGE 2
            can3 = canvas.Canvas(packet, pagesize=letter)

            can3.drawString(332, 672, 'X')
            can3.drawString(255, 656, 'property_name')
            can3.drawString(355, 656, '456')
            can3.drawString(435, 656, 'X')
            can3.drawString(520, 656, 'yes')
            can3.drawString(300, 640, 'occupancy_type')
            can3.drawString(361, 618, 'X')
            can3.drawString(300, 602, 'property_name')
            can3.drawString(255, 585, 'X')
            can3.drawString(355, 585, 'X')
            can3.drawString(435, 585, '43')
            can3.drawString(520, 585, '22')
            can3.drawString(300, 569, 'property_address')
            can3.drawString(361, 528, 'X')
            can3.drawString(255, 513, '253')
            can3.drawString(355, 513, '625')
            can3.drawString(300, 496, 'property_address')
            can3.drawString(160, 479, 'X')
            can3.drawString(231, 479, 'X')
            can3.drawString(291, 479, 'X')
            can3.drawString(300, 463, 'property_address')
            can3.drawString(256, 446, 'X')
            can3.drawString(313, 446, 'X')
            can3.drawString(381, 446, 'X')
            can3.drawString(447, 446, 'X')
            can3.drawString(506, 446, 'X')
            can3.drawString(300, 430, 'property_address')
            can3.drawString(289, 409, 'X')
            can3.drawString(255, 393, 'aj_email')
        ##    ########
            can3.drawString(355, 393, 'aj_email')
            can3.drawString(300, 377, 'property_address')
            can3.drawString(300, 360, 'property_address')
            ###
            can3.drawString(256, 342, 'X')
            can3.drawString(315, 342, 'X')
            can3.drawString(386, 342, 'X')
            can3.drawString(446, 342, 'X')
            can3.drawString(332, 323, 'X')
            can3.drawString(255, 307, '123')
            can3.drawString(355, 307, '343')
            can3.drawString(300, 290, 'aj_fax')
            can3.drawString(300, 274, 'property_address')
        ##    ########
            can3.drawString(376, 253, 'X')
            can3.drawString(300, 237, 'property_address')
            can3.drawString(220, 220, 'XER')
            can3.drawString(320, 220, 'XER')
            can3.drawString(300, 203, 'property_address')
            ########

            # second part of form
            
            can3.drawString(376, 182, 'X') 
            can3.drawString(255, 166, 'xcv')
            can3.drawString(355, 166, '233')
            ####
            can3.drawString(162, 150, 'X') 
            can3.drawString(236, 150, 'X')
            can3.drawString(300, 150, 'X')
            can3.drawString(410, 150, 'X') 
            can3.drawString(456, 150, 'X')
            ###
            can3.drawString(247, 133, 'X')
            can3.drawString(336, 133, 'X') 
            can3.drawString(404, 133, 'X')

            # SAVE PAGE 2 INPUT
            can3.save()

            # USE BEGINNING OF FILE AS PAGE REFERENCE
            packet.seek(0)
            # READ PACKET AND GET INPUT
            report_pdf = PdfFileReader(packet)


            # GET OG PAGE TO MERGE
            page_merge_4 = pdf_reader.getPage(3)
            # MERGE OG PAGE AND INPUT
            page_merge_4.mergePage(report_pdf.getPage(0))
            # ADD PAGE TO PDF
            output.addPage(page_merge_4)

        elif page == 4:

            # CREATE READABLE STREAM FROM BYTES LIKE OBJECT
            packet = io.BytesIO()

            # INPUT FOR PAGE 2
            can4 = canvas.Canvas(packet, pagesize=letter)

            can4.drawString(347, 690, 'X')
            can4.drawString(185, 674, '234')

            can4.drawString(332, 654, 'X')
            can4.drawString(255, 639, 'yes')
            can4.drawString(355, 639, 'yes')
            can4.drawString(435, 639, 'X')
            can4.drawString(515, 639, 'yes')
            can4.drawString(332, 618, 'X')
            can4.drawString(295, 602, 'XXX')
            can4.drawString(460, 602, '43')
            can4.drawString(361, 582, 'X')
            can4.drawString(260, 567, 'proper')
            can4.drawString(290, 549, 'XXX')
            can4.drawString(390, 529, 'X')
            can4.drawString(290, 512, '625')
            can4.drawString(347, 493, 'X')
            can4.drawString(290, 477, 'XXXXXXXXXXXX')
            can4.drawString(318, 428, 'X')
            can4.drawString(255, 412, 'yes')
            can4.drawString(355, 412, 'yes')
            can4.drawString(435, 412, 'X')
            can4.drawString(515, 412, 'yes')
            can4.drawString(290, 396, 'XASGVDSGF')
            can4.drawString(376, 375, 'X')
            can4.drawString(164, 358, 'X')
            can4.drawString(246, 358, 'X')
            can4.drawString(255, 342, 'yes')
            can4.drawString(355, 342, 'yes')
            can4.drawString(435, 342, 'X')
            can4.drawString(515, 342, 'yes')
            can4.drawString(290, 325, 'XDGSDGSFSD')
            ###
            can4.drawString(87, 289, 'X')
            can4.drawString(128, 289, 'X')
            can4.drawString(177, 289, 'X')
            can4.drawString(247, 289, 'X')
            can4.drawString(361, 289, 'X')
            can4.drawString(492, 289, 'X')
            can4.drawString(290, 273, 'property_address')
            can4.drawString(304, 253, 'X')
            can4.drawString(255, 237, 'Xdfg')
            can4.drawString(355, 237, 'fdgX')
            can4.drawString(290, 220, 'XDSFGDFX')
            can4.drawString(290, 203, 'XDGSDFBD')
            can4.drawString(253, 186, 'X')
            can4.drawString(313, 186, 'X')
            can4.drawString(383, 186, 'X')
            can4.drawString(444, 186, 'X')
            can4.drawString(332, 166, 'X')
            can4.drawString(290, 150, 'SDFGDSDFGSX')

            # SAVE PAGE 2 INPUT
            can4.save()

            # USE BEGINNING OF FILE AS PAGE REFERENCE
            packet.seek(0)
            # READ PACKET AND GET INPUT
            report_pdf = PdfFileReader(packet)
     
            # GET OG PAGE TO MERGE
            page_merge_5 = pdf_reader.getPage(4)
            # MERGE OG PAGE AND INPUT
            page_merge_5.mergePage(report_pdf.getPage(0))
            # ADD PAGE TO PDF
            output.addPage(page_merge_5)

        elif page == 5:

            # CREATE READABLE STREAM FROM BYTES LIKE OBJECT
            packet = io.BytesIO()

            # INPUT FOR PAGE 2
            can5 = canvas.Canvas(packet, pagesize=letter)

            can5.drawString(390, 690, 'X')
            can5.drawString(87, 655, 'X')
            can5.drawString(231, 655, 'X')
            can5.drawString(329, 655, 'X')
            can5.drawString(457, 655, 'X')
            can5.drawString(87, 638, 'X')
            can5.drawString(300, 639, 'yeelkrngrdfds')
            can5.drawString(332, 618, 'X')
            can5.drawString(300, 603, 'Xesrgsertse')
            can5.drawString(361, 582, 'X')
            can5.drawString(300, 567, 'Xsfnansgkfa')
            can5.drawString(376, 537, 'X')
            can5.drawString(300, 500, '43 sddress ln')
            can5.drawString(300, 482, 'X road lane')
            can5.drawString(300, 465, 'proper street way')
            can5.drawString(376, 416, 'X')
            can5.drawString(260, 401, 'Xds')
            can5.drawString(490, 401, '625')
            can5.drawString(220, 384, 'ewrX')
            can5.drawString(460, 384, '10')
            can5.drawString(376, 367, 'X warehouse')
            can5.drawString(300, 333, 'yes rd st')
            can5.drawString(300, 316, 'yes sir way')
            can5.drawString(300, 300, 'X address rd')
            can5.drawString(304, 280, 'X')
            can5.drawString(140, 264, 'yes')
            can5.drawString(270, 264, 'no')
            can5.drawString(365, 264, 'yes')
            can5.drawString(500, 264, 'no')
            can5.drawString(140, 245, 'yes')
            can5.drawString(270, 246, 'yes')
            can5.drawString(150, 229, 'yes')
            can5.drawString(376, 229, 'yes')
            can5.drawString(347, 210, 'X')
            can5.drawString(170, 193, '12')
            can5.drawString(280, 177, 'X warehouse, y warehouse')

            # SAVE PAGE 2 INPUT
            can5.save()

            # USE BEGINNING OF FILE AS PAGE REFERENCE
            packet.seek(0)
            # READ PACKET AND GET INPUT
            report_pdf = PdfFileReader(packet)

            # GET OG PAGE TO MERGE
            page_merge_6 = pdf_reader.getPage(5)
            # MERGE OG PAGE AND INPUT
            page_merge_6.mergePage(report_pdf.getPage(0))
            # ADD PAGE TO PDF
            output.addPage(page_merge_6)

        elif page == 6:

            # CREATE READABLE STREAM FROM BYTES LIKE OBJECT
            packet = io.BytesIO()

            # INPUT FOR PAGE 2
            can6 = canvas.Canvas(packet, pagesize=letter)

            can6.drawString(398, 710, 'X')
            can6.drawString(300, 674, 'X address ln')
            can6.drawString(300, 658, 'X address ln')
            can6.drawString(300, 641, 'X address ln')
            can6.drawString(398, 605, '15')
            can6.drawString(300, 588, 'X address ln')
            can6.drawString(300, 571, 'X address ln')
            can6.drawString(300, 554, 'X address ln')
            can6.drawString(290, 518, 'yes')
            can6.drawString(490, 518, 'yes')
            can6.drawString(170, 501, 'Xew')
            can6.drawString(380, 501, 'Xesrgsertse')
            can6.drawString(300, 485, 'X class')
            can6.drawString(87, 447, 'X')
            can6.drawString(87, 431, 'X')
            can6.drawString(318, 373, 'X')
            can6.drawString(270, 357, '13')
            can6.drawString(490, 357, '13')
            can6.drawString(380, 340, 'Xtryrss')
            can6.drawString(226, 323, 'X')
            can6.drawString(323, 323, 'X')
            can6.drawString(87, 287, 'X')
            can6.drawString(355, 271, '10')
            can6.drawString(497, 271, '50')
            can6.drawString(380, 254, 'yes rd st')
            can6.drawString(215, 237, '425')
            can6.drawString(440, 237, '234')
            can6.drawString(215, 220, '234')
            can6.drawString(310, 203, 'yes')
            can6.drawString(300, 186, 'x warehouse')

            # SAVE PAGE 2 INPUT
            can6.save()

            # USE BEGINNING OF FILE AS PAGE REFERENCE
            packet.seek(0)
            # READ PACKET AND GET INPUT
            report_pdf = PdfFileReader(packet)

            # GET OG PAGE TO MERGE
            page_merge_7 = pdf_reader.getPage(6)
            # MERGE OG PAGE AND INPUT
            page_merge_7.mergePage(report_pdf.getPage(0))
            # ADD PAGE TO PDF
            output.addPage(page_merge_7)

        elif page == 7:

            # CREATE READABLE STREAM FROM BYTES LIKE OBJECT
            packet = io.BytesIO()

            # INPUT FOR PAGE 2
            can7 = canvas.Canvas(packet, pagesize=letter)

            can7.drawString(87, 674, 'X')
            can7.drawString(200, 659, '34')
            can7.drawString(420, 658, 'X address ln')
            can7.drawString(350, 641, 'X address ln')
            can7.drawString(280, 624, 'x warehouse')
            can7.drawString(350, 608, 'X address ln')
            can7.drawString(87, 571, 'X')
            can7.drawString(240, 556, '13')
            can7.drawString(445, 555, 'x warehouse')
            can7.drawString(350, 539, 'X address ln')
            can7.drawString(280, 522, 'x warehouse')
            can7.drawString(350, 505, 'X address ln')
            can7.drawString(280, 468, 'yes js jdk  jkssfn kjet')
            can7.drawString(87, 402, 'X')
            can7.drawString(238, 402, 'X')
            can7.drawString(343, 402, 'X')
            can7.drawString(437, 402, 'X')
            can7.drawString(87, 386, 'X')
            can7.drawString(176, 387, 'X')
            can7.drawString(260, 386, 'X')
            can7.drawString(371, 387, 'X')
            can7.drawString(87, 370, 'X')
            can7.drawString(186, 370, 'X')
            can7.drawString(280, 353, 'X krsf sentkdf jntsf')
            can7.drawString(361, 333, 'X')
            can7.drawString(190, 317, '10')
            can7.drawString(280, 300, '50 eo fhaef oih')
            can7.drawString(260, 216, '345')
            can7.drawString(470, 216, '425')
            can7.drawString(260, 199, '234')
            can7.drawString(410, 199, '234')
            can7.drawString(370, 183, 'far wall')
            can7.drawString(350, 166, 'x warehouse')
            can7.drawString(390, 145, 'X')
            can7.drawString(280, 130, 'x warehouse')
            can7.drawString(240, 113, 'x waregouse')
            can7.drawString(450, 113, 'diesel')

            # SAVE PAGE 2 INPUT
            can7.save()

            # USE BEGINNING OF FILE AS PAGE REFERENCE
            packet.seek(0)
            # READ PACKET AND GET INPUT
            report_pdf = PdfFileReader(packet)

            # GET OG PAGE TO MERGE
            page_merge_8 = pdf_reader.getPage(7)
            # MERGE OG PAGE AND INPUT
            page_merge_8.mergePage(report_pdf.getPage(0))
            # ADD PAGE TO PDF
            output.addPage(page_merge_8)

        elif page == 8:

            # CREATE READABLE STREAM FROM BYTES LIKE OBJECT
            packet = io.BytesIO()

            # INPUT FOR PAGE 2
            can8 = canvas.Canvas(packet, pagesize=letter)

            can8.drawString(404, 690, 'X')
            can8.drawString(300, 674, 'Xsfd er egr gewrhgesrrg erg')
            can8.drawString(270, 657, 'Xerf fgers gd retgreg')
            can8.drawString(240, 625, '345')
            can8.drawString(460, 625, '34')
            can8.drawString(140, 588, 'x warehouse')
            can8.drawString(265, 588, 'X type')
            can8.drawString(395, 588, '333')
            can8.drawString(515, 588, '333')
            can8.drawString(240, 555, '345')
            can8.drawString(460, 555, '34')
            can8.drawString(87, 538, 'X')
            can8.drawString(290, 538, 'X')
            can8.drawString(87, 502, 'X')
            can8.drawString(265, 466, 'yes js')
            can8.drawString(485, 466, 'evacs')
            can8.drawString(240, 449, '54345 345')
            can8.drawString(425, 449, 'x warehouse')
            can8.drawString(300, 432, 'diesel ersg se,fb, ')
            can8.drawString(270, 416, 'sfdh skldf elkrt')
            can8.drawString(390, 396, 'X')
            can8.drawString(300, 379, 'X fsh dzf fdg afsh')
            can8.drawString(240, 363, '54345 345')
            can8.drawString(435, 363, 'x warehouse')
            can8.drawString(405, 343, 'X')
            can8.drawString(300, 326, 'dfkj fd;flsg ;erg;l 5/32/2344')
            can8.drawString(270, 310, 'yes js jdk  jdvd')
            can8.drawString(240, 277, '34')
            can8.drawString(455, 277, '345')
            can8.drawString(140, 240, 'x warehouse')
            can8.drawString(265, 240, 'diesel')
            can8.drawString(395, 240, '532')
            can8.drawString(515, 240, '234')
            can8.drawString(240, 207, '34')
            can8.drawString(455, 207, '54')
            can8.drawString(87, 190, 'X')
            can8.drawString(290, 190, 'X')

            # SAVE PAGE 2 INPUT
            can8.save()

            # USE BEGINNING OF FILE AS PAGE REFERENCE
            packet.seek(0)
            # READ PACKET AND GET INPUT
            report_pdf = PdfFileReader(packet)

            # GET OG PAGE TO MERGE
            page_merge_9 = pdf_reader.getPage(8)
            # MERGE OG PAGE AND INPUT
            page_merge_9.mergePage(report_pdf.getPage(0))
            # ADD PAGE TO PDF
            output.addPage(page_merge_9)

        elif page == 9:

            # CREATE READABLE STREAM FROM BYTES LIKE OBJECT
            packet = io.BytesIO()

            # INPUT FOR PAGE 2
            can9 = canvas.Canvas(packet, pagesize=letter)

            can9.drawString(347, 690, 'X')
            can9.drawString(270, 656, '3434')
            can9.drawString(490, 655, '345')
            can9.drawString(250, 638, 'X address')
            can9.drawString(410, 638, '123')
            can9.drawString(300, 622, 'x warehouse')
            can9.drawString(300, 605, 'X address ln')
            can9.drawString(390, 584, 'X')
            can9.drawString(300, 569, 'x warheoues')
            can9.drawString(235, 552, 'x warehouse')
            can9.drawString(450, 552, 'diesel')
            can9.drawString(404, 531, 'X')
            can9.drawString(300, 515, 'yes js jdk  jkssfn kjet')
            can9.drawString(300, 498, 'X fsh afsh')
            can9.drawString(230, 465, '54')
            can9.drawString(460, 465, '30')
            can9.drawString(145, 430, 'x warehouse')
            can9.drawString(265, 430, 'x type')
            can9.drawString(400, 430, '34')
            can9.drawString(515, 430, '24')
            can9.drawString(230, 396, '25')
            can9.drawString(460, 396, '64')
            can9.drawString(87, 378, 'X')
            can9.drawString(289, 378, 'X')
            can9.drawString(133, 303, 'X')
            can9.drawString(205, 303, 'X')
            can9.drawString(460, 304, '50087079')
            can9.drawString(87, 270, 'X')
            can9.drawString(200, 271, '345')
            can9.drawString(87, 253, 'X')
            can9.drawString(320, 254, '234')
            can9.drawString(89, 236, 'X')
            can9.drawString(280, 221, 'far wall over ther, cabfjkr s ekgjbaefjb rj')
            can9.drawString(350, 204, 'x warehouse')
            can9.drawString(175, 171, 'X nf nsfm')
            can9.drawString(350, 171, 'connor burk')
            can9.drawString(490, 171, '5/23/1998')
            can9.drawString(180, 154, 'X nf nsfm')
            can9.drawString(345, 154, 'connor burk')
            can9.drawString(490, 154, '5/23/1998') 
            # SAVE PAGE 2 INPUT
            can9.save()

            # USE BEGINNING OF FILE AS PAGE REFERENCE
            packet.seek(0)
            # READ PACKET AND GET INPUT
            report_pdf = PdfFileReader(packet)

            # GET OG PAGE TO MERGE
            page_merge_10 = pdf_reader.getPage(9)
            # MERGE OG PAGE AND INPUT
            page_merge_10.mergePage(report_pdf.getPage(0))
            # ADD PAGE TO PDF
            output.addPage(page_merge_10)

        elif page == 10:

            # CREATE READABLE STREAM FROM BYTES LIKE OBJECT
            packet = io.BytesIO()

            # INPUT FOR PAGE 2
            can10 = canvas.Canvas(packet, pagesize=letter)

            can10.drawString(87, 690, 'X')
            can10.drawString(87, 637, 'X')
            can10.drawString(87, 584, 'X')
            can10.drawString(190, 584, '345')
            can10.drawString(87, 567, 'X')
            can10.drawString(340, 568, '234')
            can10.drawString(89, 550, 'X')
            can10.drawString(260, 534, 'X sgfkjg dfg fpoisg egpnertjp  egpjn')
            can10.drawString(89, 517, 'X')
            can10.drawString(160, 489, 'x warehouse')
            can10.drawString(350, 489, 'diesel ersg')
            can10.drawString(485, 489, '5/32/2344')
            can10.drawString(160, 472, 'yes js jdk  jdvd')
            can10.drawString(330, 472, 'X fsh dzf fdg afsh')
            can10.drawString(485, 472, '54345 345')

            can10.drawString(160, 379, 'x warehouse')
            can10.drawString(350, 379, 'diesel ersg')
            can10.drawString(485, 379, '5/32/2344')
            can10.drawString(160, 361, 'yes js jdk  jdvd')
            can10.drawString(330, 361, 'X fsh dzf fdg afsh')
            can10.drawString(485, 362, '54345 345')

            can10.drawString(160, 298, 'x warehouse')
            can10.drawString(350, 298, 'diesel ersg')
            can10.drawString(485, 298, '5/32/2344')
            can10.drawString(160, 280, 'yes js jdk  jdvd')
            can10.drawString(330, 280, 'X fsh dzf fdg afsh')
            can10.drawString(485, 281, '54345 345')

            can10.drawString(160, 216, 'x warehouse')
            can10.drawString(350, 216, 'diesel ersg')
            can10.drawString(485, 216, '5/32/2344')
            can10.drawString(160, 199, 'yes js jdk  jdvd')
            can10.drawString(330, 199, 'X fsh dzf fdg afsh')
            can10.drawString(485, 200, '54345 345')
            

            # SAVE PAGE 2 INPUT
            can10.save()

            # USE BEGINNING OF FILE AS PAGE REFERENCE
            packet.seek(0)
            # READ PACKET AND GET INPUT
            report_pdf = PdfFileReader(packet)

            # GET OG PAGE TO MERGE
            page_merge_11 = pdf_reader.getPage(10)
            # MERGE OG PAGE AND INPUT
            page_merge_11.mergePage(report_pdf.getPage(0))
            # ADD PAGE TO PDF
            output.addPage(page_merge_11)

        elif page == 11:

            # CREATE READABLE STREAM FROM BYTES LIKE OBJECT
            packet = io.BytesIO()

            # INPUT FOR PAGE 2
            can11 = canvas.Canvas(packet, pagesize=letter)

            can11.drawString(170, 646, 'X sdfsg sf')
            can11.drawString(350, 646, 'dfjs sdflk sjfl')
            can11.drawString(485, 646, '5/23/5343')
            can11.drawString(160, 629, '345 shf jsdlklkjd')
            can11.drawString(310, 629, '34kfdhsjk kjfsdkfjlsdhf')
            can11.drawString(480, 629, '6289348989')

            can11.drawString(170, 544, 'X sdfsg sf')
            can11.drawString(350, 544, 'dfjs sdflk sjfl')
            can11.drawString(485, 544, '5/23/5343')
            can11.drawString(160, 527, '345 shf jsdlklkjd')
            can11.drawString(310, 527, '34kfdhsjk kjfsdkfjlsdhf')
            can11.drawString(480, 527, '6289348989')

            # SAVE PAGE 2 INPUT
            can11.save()

            # USE BEGINNING OF FILE AS PAGE REFERENCE
            packet.seek(0)
            # READ PACKET AND GET INPUT
            report_pdf = PdfFileReader(packet)
     
            # GET OG PAGE TO MERGE
            page_merge_12 = pdf_reader.getPage(11)
            # MERGE OG PAGE AND INPUT
            page_merge_12.mergePage(report_pdf.getPage(0))
            # ADD PAGE TO PDF
            output.addPage(page_merge_12)


    #'property_name' = 'test_prop1'
    date = str(datetime.date.today())
    date.replace(' ', '')

    directory = "C:/Users/Connor/Desktop/DesktopAPP/GEORGE ALARM CO/reports/" + 'property_name'
    if not os.path.exists(directory):
        os.makedirs(directory)
            
    file_name = property_name + '_' + date + '.pdf'
    path_to_file = pjoin(directory, file_name)
    path_to_file.replace('"/"', '"\\"')
    outputStream = open(path_to_file, 'ab+')
    output.write(outputStream)
    outputStream.close()
    
prop_name = 'james_watters'
write_on_pdf(prop_name)
