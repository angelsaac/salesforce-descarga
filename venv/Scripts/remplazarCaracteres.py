#importing pandas module 
import pandas as pd
import sys 
ruta = "//10.50.2.99/xampp/htdocs/reportes_automaticos_salesforce/Lib/site-packages"
sys.path.append(ruta)

def eliminarAcentos(report_df,nombreColumnas):
    # creating dictionary for trans table
    trans_dict ={
    "Á": "A",
    "À": "A",
    "Â": "A",
    "Ä": "A",
    "á": "a",
    "à": "a",
    "ä" : "a",
    "â" : "a", 
    "ª": "a"
    ,"É":"E"
    ,"È":"E"
    ,"Ê":"E"
    ,"Ë":"E"
    ,"é":"e"
    ,"è":"e"
    ,"ë":"e"
    ,"ê":"e"
    ,"Í":"I"
    ,"Ì":"I"
    , "Ï":"I"
    , "Î":"I"
    , "í":"i"
    , "ì":"i"
    , "ï": "i"
    , "î": "i"
    ,"Ó":"O", "Ò": "O", "Ö": "O", "Ô": "O", "ó": "o", "ò": "o", "ö":"o", "ô": "o"
    ,"Ú": "U", "Ù":"U", "Û":"U", "Ü":"U", "ú": "u", "ù": "u", "ü": "u", "û": "u"
    ,"Ñ": "N", "ñ":"n", "Ç": "C", "ç": "c", "Ð":"N", "Č": "C", "ř":"r" , "ň": "n"  
    ,"\'":'', "!": '', "°": "",  "|":"", "!":"",  "\"": "", "$": "", "%":"", "&": "", "(":"", ")":"", "=": "", "?": "", "¡":"" , ".": "", "¿":"", "¨": "", "´":"", "*":"", "+":"" , "[": "", "{": "", "]": "", "}": "", ",": "", ";":"", "_": "", "<": "", ">": "", "@": "", "%": ""
    ,"😁": "", "😀":"", "😇": "", "😈": "", "😎": "", "😐": "", "😑":"", "😕":"", "😗":"", "😙": "", "😛":"", "😟":"", "😦": "", "😧": "", "😬":"", "😮": "", "😯":"", "😴" :"","😶":"","😁":"","😀":"","😇":"","😈":"","😎":"","😐":"","😑":"","😕":"","😗":"","😙":"","😛":"","😟": "","😦":"" , "😧":"", "😬":"", "😮" :"","😯" :"","😴":"", "😶" :""
    ,"🚁" :"","🚂" :"","🚆":"", "🚈" :"","🚊":"", "🚍":"", "🚎":"", "🚐" :"","🚔" :"","🚖":"", "🚘" :"","🚛" :"","🚜":"", "🚝":"","🚞":"", "🚟" :"","🚠" :"","🚡":"", "🚣":"", "🚦" :"","🚮" :"","🚯":"","🚰":"","🚱":"","🚳":"","🚴":""
    ,"🚵":"","🚷":"","🚸":"","🚿":"","🛁":"","🛂":"","🛃":"","🛄":"","🛅":"","🌍":"","🌎":"","🌐":"","🌒":"","🌖":"","🌗":"","🌘":"","🌚":"","🌜":"","🌝":"","🌞":"","🌲":""
    ,"🌳":"","🍋":"","🍐":"","🍼":"","🏇":"","🏉":"","🏤":"","🐀":"","🐁":"","🐂":"","🐃":"","🐄":"","🐅":"","🐆":"","🐇":""
    ,"🐈":"","🐉":"","🐊":"","🐋":"","🐏":"","🐐":"","🐓":"","🐕":"","🐖":"","🐪":"","👥":"","👬":"","👭":"","💭":"","💶":"","💷":"","📬":"","📭":"","📯":""
    ,"📵":"","🔀":"","🔁":"","🔂":"","🔄":"","🔅":"","🔆":"","🔇":"","🔉":"","🔕":"","🔬":"","🔭":"","🕜":"","🕝":"","🕞":"","🕟":"","🕠":"","🕡":""
    ,"🕢":"","🕣":"","🕤":"","🕥":"","🕦":"","🕧":"","😁":"","😂":"","😃":"","😄":"","😅":"","😆":"","😉":"","😊":"","😋":"","😌":"","😍":""
    ,"😏":"","😒":"","😓":"","😔":"","😖":"","😘":"","😚":"","😜":"","😝":"","😞":"","😠":"","😡":"","😢":"","😣":"","😤":"","😥":"","😨":""
    ,"😩":"","😪":"","😫":"","😭":"","😰":"","😱":"","😲":"","😳":"","😵":"","😷":"","😸":"","😹":"","😺":"","😻":"","😼":"","😽":"","😾":"","😿":"","🙀":""
    ,"🙅":"","🙆":"","🙇":"","🙈":"","🙉":"","🙊":"","🙋":"","🙌":"","🙍":"","🙎":"","🙏":"","✂":"","✅":"","✈":"","✉":"","✊":"","✋":"","✌":"","✏":"","✒":"","✔":"","✖":"","✨":"","✳":"","✴":"","❄":"","❇":"","❌":"","❎":""
    ,"❓":"","❔":"","❕":"","❗":"","❤":"","➕":"","➖":"","➗":"","➡":"","➰":"","🚀":"","🚃":"","🚄":"","🚅":"","🚇":"","🚉":""
    ,"🚌":"","🚏":"","🚑":"","🚒":"","🚓":"","🚕":"","🚗":"","🚙":"","🚚":"","🚢":"","🚤":"","🚥":"","🚧":"","🚨":"","🚩":"","🚪":"","🚫":"","🚬":"","🚭":"","🚲":"","🚶":"","🚹":""
    ,"🚺":"","🚻":"","🚼":"","🚽":"","🚾":"","🛀":"","Ⓜ":"","🅰":"","🅱":"","🅾":"","🅿":"","🆎":"","🆑":"","🆒":"","🆓":"","🆔":"","🆕":"","🆖":"","🆗":"","🆘":"","🆙":"","🆚":""
    ,"🈁":"","🈂":"","🈚":"","🈯":"","🈲":"","🈳":"","🈴":"","🈵":"","🈶":"","🈷":"","🈸":"","🈹":"","🈺":""
    ,"🉐":"","🉑":"","©":"","®":"","‼":"","⁉":"", "™":"", "ℹ":"","↔":"","↕":""
    ,"↖":"","↗":"","↘":"","↙":"","↩":"","↪":"","⌚":"","⌛":"","⏩":"","⏪":"","⏫":"","⏬":"","⏰":"","⏳":"","▪":"","▫":"","▶":"","◀":"","◻":"","◼":"","◽":""
    ,"◾":"","☀":"","☁":"","☎":"","☑":"","☔":"","☕":"","☝":"","☺":"","♈":"","♉":"","♊":"","♋":"","♌":"","♍":"","♎":"","♏":"","♐":"","♑":"","♒":"","♓":"","♠":""
    ,"♣":"","♥":"","♦":"","♨":"","♻":"","♿":"","⚓":"","⚠":"","⚡":"","⚪":"","⚫":"","⚽":"","⚾":"","⛄":"","⛅":"","⛎":"","⛔":"","⛪":"","⛲":"","⛳":"","⛵":"","⛺":""
    ,"⛽":"","⤴":"","⤵":"","⬅":"","⬆":"","⬇":"","⬛":"","⬜":"","⭐":"","⭕":"","〰":"","〽":"","㊗":"","㊙":"","🀄":"","🃏":"","🌀":"","🌁":"","🌂":"","🌃":"","🌄":"","🌅":"","🌆":"","🌇":""
    ,"🌈":"","🌉":"","🌊":"","🌋":"","🌌":"","🌏":"","🌑":"","🌓":"","🌔":"","🌕":"","🌙":"","🌛":"","🌟":"","🌠":"","🌰":"","🌱":"","🌴":"","🌵":"","🌷":"","🌸":"","🌹":""
    ,"🌺":"","🌻":"","🌼":"","🌽":"","🌾":"","🌿":"","🍀":"","🍁":"","🍂":"","🍃":"","🍄":"","🍅":"","🍆":"","🍇":"","🍈":"","🍉":"","🍊":"","🍌":""
    ,"🍍":"","🍎":"","🍏":"","🍑":"","🍒":"","🍓":"","🍔":"","🍕":"","🍖":"","🍗":"","🍘":"","🍙":"" ,"🍚":"","🍛":"","🍜":"","🍝":"","🍞":"","🍟":"","🍠":"","🍡":""
    ,"🍢":"","🍣":"","🍤":"","🍥":"","🍦":"","🍧":"","🍨":"","🍩":"","🍪":"","🍫":"","🍬":"","🍭":"","🍮":"","🍯":"","🍰":"","🍱":"","🍲":"","🍳":"","🍴":"","🍵":"","🍶":"","🍷":""
    ,"🍸":"","🍹":"","🍺":"","🍻":"","🎀":"","🎁":"","🎂":"","🎃":"","🎄":"","🎅":"","🎆":"","🎇":"","🎈":"","🎉":"","🎊":""
    ,"🎋":"","🎌":"","🎍":"","🎎":"","🎏":"","🎐":"","🎑":"","🎒":"","🎓":"","🎠":"","🎡":"","🎢":"","🎣":"","🎤":"","🎥":"","🎦":""
    ,"🎧":"","🎨":"","🎩":"","🎪":"","🎫":"","🎬":"","🎭":"","🎮":"","🎯":"","🎰":"","🎱":"","🎲":"","🎳":"","🎴":"","🎵":"","🎶":"" ,"🎷":""
    ,"🎸":"","🎹":"","🎺":"","🎻":"","🎼":"","🎽":"","🎾":"","🎿":"","🏀":"","🏁":"","🏂":"","🏃":"","🏄":"","🏆":"","🏈":"","🏊":"","🏠":"","🏡":"","🏢":"","🏣":"","🏥":"","🏦":"","🏧":"","🏨":"","🏩":"","🏪":""
    ,"🏫":"","🏬":"","🏭":"","🏮":"","🏯":"","🏰":"","🐌":"","🐍":"","🐎":"","🐑":"","🐒":"","🐔":"","🐗":"","🐘":"","🐙":"","🐚":"","🐛":"","🐜":"","🐝":""
    ,"🐞":"","🐟":"","🐠":"","🐡":"","🐢":"","🐣":"","🐤":"","🐥":"","🐦":"","🐧":"","🐨":"","🐩":"","🐫":"","🐬":"","🐭":"","🐮":"","🐯":"","🐰":"","🐱":"","🐲":"","🐳":"","🐴":"","🐵":"","🐶":"","🐷":"","🐸":"","🐹":"","🐺":"","🐻":"","🐼":""
    ,"🐽":"","🐾":"","👀":"","👂":"","👃":"","👄":"","👅":"","👆":"","👇":"","👈":"","👉":"","👊":"","👋":"" ,"👌":"","👍":"","👎":"","👏":"","👐":"","👑":"","👒":"","👓":"","👔":"","👕":"","👖":""
    ,"👗":"","👘":"","👙":"","👚":"","👛":"","👜":"","👝":"","👞":"","👟":"","👠":"","👡":"","👢":"","👣":"","👤":"","👦":"","👧":"","👨":"","👩":"","👪":"","👫":"","👮":""
    ,"👯":"","👰":"","👱":"","👲":"","👳":"","👴":"","👵":"","👶":"" ,"👷":"","👸":"" ,"👹":"","👺":"","👻":"","👼":"","👽":"","👾":"","👿":"","💀":"","💁":"","💂":""
    ,"💃":"","💄":"","💅":"","💆":"","💇":"","💈":"","💉":"","💊":"","💋":"","💌":"","💍":"","💎":"","💏":"","💐":"","💑":"","💒":"","💓":"","💔":"","💕":"","💖":"","💗":"","💘":"","💙":"","💚":"","💛":"","💜":"","💝":"","💞":"","💟":"","💠":"","💡":"","💢":"","💣":""
    ,"💤":"","💥":"","💦":"","💧":"","💨":"","💩":"","💪":"","💫":"","💬":"","💮":"","💯":"","💰":"","💱":"","💲":"","💳":"","💴":"","💵":"","💸":"","💹":"","💺":"","💻":"","💼":"","💽":"","💾":"","💿":"","📀":"","📁":"","📂":"","📃":"","📄":"","📅":"","📆":"","📇":"","📈":"","📉":"","📊":"","📋":"","📌":""
    ,"📍":"","📎":"","📏":"","📐":"","📑":"","📒":"","📓":"","📔":"","📕":"","📖":"","📗":"","📘":"","📙":"","📚":"","📛":"","📜":"","📝":"","📞":"","📟":"","📠":"","📡":"","📢":"","📣":"","📤":"","📥":"","📦":"","📧":"" ,"📨":"","📩":"" ,"📪":"","📫":"","📮":"","📰":"","📱":""
    ,"📲":"","📳":"","📴":"","📶":"","📷":"","📹":"","📺":"","📻":"","📼":"","🔃":"","🔊":"","🔋":"","🔌":"","🔍":"","🔎":"","🔏":"","🔐":"","🔑":"","🔒":"","🔓":"","🔔":"","🔖":"","🔗":"","🔘":"","🔙":"","🔚":"","🔛":""
    ,"🔜":"","🔝":"","🔞":"","🔟":"","🔠":"","🔡":"","🔢":"","🔣":"","🔤":"","🔥":"","🔦":"","🔧":"","🔨":"","🔩":"","🔪":"","🔫":"","🔮":"","🔯":"","🔰":"","🔱":"","🔲":"","🔳":"","🔴":"","🔵":"","🔶":"" 
    ,"🔷":"","🔸":"","🔹":"","🔺":"","🔻":"","🔼":"","🔽":"","🕐":"","🕑":"","🕒":"","🕓":"","🕔":"","🕕":"" ,"🕖":"" ,"🕗":"","🕘":"","🕙":"" ,"🕚":"" ,"🕛":"","🗻":"","🗼":"","🗽":"","🗾":"","🗿":"","🤍": "", "🖤": "", "ø":"", "ل": "", "إ":"","ã":"","🫀":""
    }

    trans_table ="ÁÀÂÄáàäâªÉÈÊËéèëêÍÌÏÎíìïîÓÒÖÔóòöôÚÙÛÜúùüûÑñÇçÐČřň\'!°|!\"$%&()=?¡.¿¨´*+[{]},;_<>@%😁😀😇😈😎😐😑😕😗😙😛😟😦😧😬😮😯😴😶😁😀😇😈😎😐😑😕😗😙😛😟😦😧😬😮😯😴😶🚁🚂🚆🚈🚊🚍🚎🚐🚔🚖🚘🚛🚜🚝🚞🚟🚠🚡🚣🚦🚮🚯🚰🚱🚳🚴🚵🚷🚸🚿🛁🛂🛃🛄🛅🌍🌎🌐🌒🌖🌗🌘🌚🌜🌝🌞🌲🌳🍋🍐🍼🏇🏉🏤🐀🐁🐂🐃🐄🐅🐆🐇🐈🐉🐊🐋🐏🐐🐓🐕🐖🐪👥👬👭💭💶💷📬📭📯📵🔀🔁🔂🔄🔅🔆🔇🔉🔕🔬🔭🕜🕝🕞🕟🕠🕡🕢🕣🕤🕥🕦🕧😁😂😃😄😅😆😉😊😋😌😍😏😒😓😔😖😘😚😜😝😞😠😡😢😣😤😥😨😩😪😫😭😰😱😲😳😵😷😸😹😺😻😼😽😾😿🙀🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏✂✅✈✉✊✋✌✏✒✔✖✨✳✴❄❇❌❎❓❔❕❗❤➕➖➗➡➰🚀🚃🚄🚅🚇🚉🚌🚏🚑🚒🚓🚕🚗🚙🚚🚢🚤🚥🚧🚨🚩🚪🚫🚬🚭🚲🚶🚹🚺🚻🚼🚽🚾🛀Ⓜ🅰🅱🅾🅿🆎🆑🆒🆓🆔🆕🆖🆗🆘🆙🆚🈁🈂🈚🈯🈲🈳🈴🈵🈶🈷🈸🈹🈺🉐🉑©®‼⁉™ℹ↔↕↖↗↘↙↩↪⌚⌛⏩⏪⏫⏬⏰⏳▪▫▶◀◻◼◽◾☀☁☎☑☔☕☝☺♈♉♊♋♌♍♎♏♐♑♒♓♠♣♥♦♨♻♿⚓⚠⚡⚪⚫⚽⚾⛄⛅⛎⛔⛪⛲⛳⛵⛺⛽⤴⤵⬅⬆⬇⬛⬜⭐⭕〰〽㊗㊙🀄🃏🌀🌁🌂🌃🌄🌅🌆🌇🌈🌉🌊🌋🌌🌏🌑🌓🌔🌕🌙🌛🌟🌠🌰🌱🌴🌵🌷🌸🌹🌺🌻🌼🌽🌾🌿🍀🍁🍂🍃🍄🍅🍆🍇🍈🍉🍊🍌🍍🍎🍏🍑🍒🍓🍔🍕🍖🍗🍘🍙🍚🍛🍜🍝🍞🍟🍠🍡🍢🍣🍤🍥🍦🍧🍨🍩🍪🍫🍬🍭🍮🍯🍰🍱🍲🍳🍴🍵🍶🍷🍸🍹🍺🍻🎀🎁🎂🎃🎄🎅🎆🎇🎈🎉🎊🎋🎌🎍🎎🎏🎐🎑🎒🎓🎠🎡🎢🎣🎤🎥🎦🎧🎨🎩🎪🎫🎬🎭🎮🎯🎰🎱🎲🎳🎴🎵🎶🎷🎸🎹🎺🎻🎼🎽🎾🎿🏀🏁🏂🏃🏄🏆🏈🏊🏠🏡🏢🏣🏥🏦🏧🏨🏩🏪🏫🏬🏭🏮🏯🏰🐌🐍🐎🐑🐒🐔🐗🐘🐙🐚🐛🐜🐝🐞🐟🐠🐡🐢🐣🐤🐥🐦🐧🐨🐩🐫🐬🐭🐮🐯🐰🐱🐲🐳🐴🐵🐶🐷🐸🐹🐺🐻🐼🐽🐾👀👂👃👄👅👆👇👈👉👊👋👌👍👎👏👐👑👒👓👔👕👖👗👘👙👚👛👜👝👞👟👠👡👢👣👤👦👧👨👩👪👫👮👯👰👱👲👳👴👵👶👷👸👹👺👻👼👽👾👿💀💁💂💃💄💅💆💇💈💉💊💋💌💍💎💏💐💑💒💓💔💕💖💗💘💙💚💛💜💝💞💟💠💡💢💣💤💥💦💧💨💩💪💫💬💮💯💰💱💲💳💴💵💸💹💺💻💼💽💾💿📀📁📂📃📄📅📆📇📈📉📊📋📌📍📎📏📐📑📒📓📔📕📖📗📘📙📚📛📜📝📞📟📠📡📢📣📤📥📦📧📨📩📪📫📮📰📱📲📳📴📶📷📹📺📻📼🔃🔊🔋🔌🔍🔎🔏🔐🔑🔒🔓🔔🔖🔗🔘🔙🔚🔛🔜🔝🔞🔟🔠🔡🔢🔣🔤🔥🔦🔧🔨🔩🔪🔫🔮🔯🔰🔱🔲🔳🔴🔵🔶🔷🔸🔹🔺🔻🔼🔽🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛🗻🗼🗽🗾🗿🤍🖤øإلã🫀".maketrans(trans_dict)
    report_df[nombreColumnas]= report_df[nombreColumnas].str.translate(trans_table)
    return report_df[nombreColumnas]

