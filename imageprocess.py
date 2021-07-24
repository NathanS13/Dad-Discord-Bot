import urllib.request
import json
import ast
from PIL import Image, ImageDraw, ImageFont
def pullImages(itemList):
    itemList = ast.literal_eval(itemList)
    for item in itemList:
        if (item != 'EMPTY'):
            url = 'https://render.albiononline.com/v1/item/' + item + '.png'
            operUrl = urllib.request.urlretrieve(url, 'itemimage/' + item + '.png')

def generateImage(itemList):
    itemList = ast.literal_eval(itemList)

    width = 600
    height = 900

    background = Image.new(mode = "RGB", size = (width, height), color = (245, 245, 220))
    bg_w, bg_h = background.size


    #default = Image.open('itemimage/Grey_box.png')


    weapon = Image.open('itemimage/' + itemList[0] + '.png')
    offhand = Image.open('itemimage/' + itemList[1] + '.png')
    helmet = Image.open('itemimage/' + itemList[2] + '.png')
    chest = Image.open('itemimage/' + itemList[3] + '.png')
    shoes = Image.open('itemimage/' + itemList[4] + '.png')
    bag = Image.open('itemimage/' + itemList[5] + '.png')
    cape = Image.open('itemimage/' + itemList[6] + '.png')
    mount = Image.open('itemimage/' + itemList[7] + '.png')
    potion = Image.open('itemimage/' + itemList[8] + '.png')
    food = Image.open('itemimage/' + itemList[9] + '.png')

    if ('2H' in itemList[0]):
        offhand = Image.open('itemimage/' + itemList[0] + '.png')
        alpha = offhand.getchannel('A')
        newAlpha = alpha.point(lambda i: 128 if i>90 else 0)
        offhand.putalpha(newAlpha)


    #default = Image.open('itemimage/Grey_box.png')
    #helmet = Image.open('itemimage/' + itemList[5] + '.png')
    #helmet = Image.open('itemimage/' + itemList[5] + '.png')

    imageSize = (200,200)
    weapon = weapon.resize(imageSize)
    offhand = offhand.resize(imageSize)
    helmet = helmet.resize(imageSize)
    chest = chest.resize(imageSize)
    shoes = shoes.resize(imageSize)
    bag = bag.resize(imageSize)
    cape = cape.resize(imageSize)
    mount = mount.resize(imageSize)
    potion = potion.resize(imageSize)
    food = food.resize(imageSize)




    img_w, img_h = weapon.size


    #offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    offsetWep = (0, 250)
    offsetOffhand = (400, 250)
    offsetHelmet = (200, 50)
    offsetChest = (200, 250)
    offsetShoes = (200, 450)
    offsetBag = (0, 50)
    offsetCape = (400, 50)
    offsetMount = (200, 650)
    offsetPotion = (0, 450)
    offsetFood = (400, 450)

    #offsetRibbon = ()


    background.paste(weapon, offsetWep, weapon)
    background.paste(offhand, offsetOffhand, offhand)
    background.paste(helmet, offsetHelmet, helmet)
    background.paste(chest, offsetChest, chest)
    background.paste(shoes, offsetShoes, shoes)
    background.paste(bag, offsetBag, bag)
    background.paste(cape, offsetCape, cape)
    background.paste(mount, offsetMount, mount)
    background.paste(potion, offsetFood, potion)
    background.paste(food, offsetPotion, food)
    #png_info = img.info
    #background.save('2.png', **png_info)

    #background.show()
    #background.save('test.png')
    return background

def mergeKill(image1, image2, playername, victimname, fame, killip, victimip):
    width = 1300
    height = 930

    background = Image.new(mode = "RGB", size = (width, height), color = (245, 245, 220))
    bg_w, bg_h = background.size

    background.paste(image1, (0,0))
    background.paste(image2, (700,0))

    lineimg = ImageDraw.Draw(background)
    lineimg.line([(650,100),(650,800)], fill ="black", width = 0)


    title_font = ImageFont.truetype('sanstext.ttf', 30)
    title_fontsmall = ImageFont.truetype('sanstext.ttf', 26)
    title_fontsmaller = ImageFont.truetype('sanstext.ttf', 14)

    strip_width, strip_height = 600, 50
    text = playername
    center_text(background, title_font, text, strip_width, strip_height, 0, 0)

    strip_width, strip_height = 600, 50
    text = victimname
    center_text(background, title_font, text, strip_width, strip_height, 700, 0)

    strip_width, strip_height = 100, 50
    text = 'Killed'
    center_text(background, title_font, text, strip_width, strip_height, 600, 0)

    ribbon = Image.open('itemimage/RIBBON.png')
    ribbon = ribbon.resize((40,40))
    strip_width, strip_height = 100, 50
    tempFame = int(fame)
    text  = str("{:,}".format(tempFame))
    center_text(background, title_fontsmall, text, strip_width, strip_height, 600, 840)
    pos = getpos(background, title_fontsmall, text, strip_width, strip_height, 600, 840)
    offsetRibbon = (int(pos[0]) - 50, 850)
    background.paste(ribbon, offsetRibbon, ribbon)


    strip_width, strip_height = 150, 50
    text = 'Avg IP: ' + str(round(float(killip)))
    center_text(background, title_fontsmall, text, strip_width, strip_height, 0, 840)

    strip_width, strip_height = 150, 50
    text = 'Avg IP: ' + str(round(float(victimip)))
    center_text(background, title_fontsmall, text, strip_width, strip_height, 1150, 840)

    strip_width, strip_height = 100, 20
    text = 'Created by Mushy'
    center_text(background, title_fontsmaller, text, strip_width, strip_height, 600, 900)


    #title_text = playername
    #image_editable = ImageDraw.Draw(background)
    #image_editable.text((250,7.5), title_text, (54, 69, 79), font=title_font)

    #title_text = victimname
    #image_editable = ImageDraw.Draw(background)
    #image_editable.text((1000,7.5), title_text, (54, 69, 79), font=title_font)


    #background.show()
    #background.save('test3.png')
    return background

def center_text(img, font, text, strip_width, strip_height, offset, offsety, color=(54, 69, 79)):
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)
    position = ((strip_width-text_width)/2 + offset,(strip_height-text_height)/2 + offsety)
    draw.text(position, text, color, font=font)
    return img

def getpos(img, font, text, strip_width, strip_height, offset, offsety):
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)
    position = ((strip_width-text_width)/2 + offset,(strip_height-text_height)/2 + offsety)
    return position


#itemList = ['2769803', 'Weever', ['T4_2H_IRONGAUNTLETS_HELL@2', 'EMPTY', 'T4_HEAD_LEATHER_SET3@2', 'T5_ARMOR_CLOTH_SET2@1', 'T4_SHOES_LEATHER_HELL@2', 'T4_BAG', 'T4_CAPEITEM_FW_THETFORD@2', 'T3_MOUNT_HORSE', 'EMPTY', 'EMPTY'], ['T4_2H_IRONGAUNTLETS_HELL@2', 'EMPTY', 'T6_HEAD_LEATHER_SET3', 'T4_ARMOR_CLOTH_SET2@1', 'T5_SHOES_LEATHER_HELL@1', 'T4_BAG@1', 'T2_CAPE', 'T2_MOUNT_MULE', 'EMPTY', 'EMPTY']]
#itemList2 = ['T4_2H_IRONGAUNTLETS_HELL@2', 'EMPTY', 'T4_HEAD_LEATHER_SET3@2', 'T5_ARMOR_CLOTH_SET2@1', 'T4_SHOES_LEATHER_HELL@2', 'T4_BAG', 'T4_CAPEITEM_FW_THETFORD@2', 'T3_MOUNT_HORSE', 'EMPTY', 'EMPTY']
#itemList33= ['100', 'weever', ['T6_2H_SPEAR', 'T5_HEAD_PLATE_HELL@1', 'T5_ARMOR_CLOTH_SET2@1', 'T5_SHOES_LEATHER_SET2@1', 'T4_BAG', 'T4_CAPEITEM_DEMON@1', 'T3_MOUNT_HORSE'], ['T4_2H_IRONGAUNTLETS_HELL@2', 'T6_HEAD_LEATHER_SET3', 'T4_ARMOR_CLOTH_SET2@1', 'T5_SHOES_LEATHER_HELL@1', 'T4_BAG@1', 'T2_CAPE', 'T2_MOUNT_MULE']]
#itemList3 = ['T4_2H_IRONGAUNTLETS_HELL@2', 'EMPTY', 'T6_HEAD_LEATHER_SET3', 'T4_ARMOR_CLOTH_SET2@1', 'T5_SHOES_LEATHER_HELL@1', 'T4_BAG@1', 'T2_CAPE', 'T2_MOUNT_MULE', 'EMPTY', 'EMPTY']
#itemList="['T6_2H_CLAWPAIR', 'EMPTY', 'T5_HEAD_CLOTH_SET3', 'T5_ARMOR_LEATHER_SET3', 'T6_SHOES_LEATHER_SET1', 'T4_BAG@1', 'T4_CAPEITEM_DEMON@2', 'T3_MOUNT_HORSE', 'T6_POTION_COOLDOWN', 'T8_MEAL_STEW@1']"
#itemList2="['T4_2H_IRONGAUNTLETS_HELL@2', 'EMPTY', 'T4_HEAD_LEATHER_SET3@2', 'T5_ARMOR_CLOTH_SET2@1', 'T4_SHOES_LEATHER_HELL@2', 'T4_BAG', 'T4_CAPEITEM_FW_THETFORD@2', 'T3_MOUNT_HORSE', 'EMPTY', 'EMPTY']"
#pullImages(itemList)
#pullImages(itemList2)
#image1 = generateImage(itemList)
#image2 = generateImage(itemList2)
#mergeKill(image1, image2, 'Mushii', 'weever', '123123', '900', '950')
