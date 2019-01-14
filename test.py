import time
import json
import iqoption as iq

iqStream = iq.IQOption(active_id="EURUSD")


profile = iqStream.api.getprofile()#api.getprofile()
print profile._content
res = json.loads(profile._content)
balance = res['name']['profile']

#{"isSuccessful":true,"message":"","result":{"avatar":"http:\/\/graph.facebook.com\/10208062541311740\/picture?type=large","confirmation_required":0,"popup":[],"money":{"deposit":{"min":2,"max":1000000},"withdraw":{"min":2,"max":1000000}},"user_group":"VIP","welcome_splash":0,"functions":{"is_bonus_block":0,"is_trading_bonus_block":0,"is_vip_mode":0,"is_no_currency_change":0,"popup_ids":[""],"ext_fields":[]},"finance_state":"","balance":9,"bonus_wager":0,"bonus_total_wager":0,"balance_id":7780034,"balance_type":1,"messages":0,"id":7572160,"practice":0,"public":1,"group_id":3,"name":"Lorenzo Argentieri","nickname":null,"currency":"EUR","currency_char":"\u20ac","mask":"\u20ac %s","city":"london","user_id":7572160,"first_name":"Lorenzo","last_name":"Argentieri","phone":"39 3450990971","email":"uni.lorenzo.a@gmail.com","created":1450694426,"last_visit":false,"site_id":1,"tz":"Europe\/London","locale":"it_IT","birthdate":639777600,"country_id":206,"currency_id":1,"gender":"male","address":"2G Doric Way","postal_index":"NW1 1LX","timediff":-7200,"tz_offset":60,"balances":[{"id":7780034,"type":1,"amount":9000000,"new_amount":9000000,"bonus_amount":0,"bonus_total_amount":0,"currency":"EUR","description":null},{"id":35924583,"type":2,"amount":240000,"new_amount":0,"bonus_amount":0,"bonus_total_amount":0,"currency":"USD","description":null},{"id":35924580,"type":2,"amount":80000000,"new_amount":0,"bonus_amount":0,"bonus_total_amount":0,"currency":"USD","description":null},{"id":21949793,"type":2,"amount":190000,"new_amount":0,"bonus_amount":0,"bonus_total_amount":0,"currency":"USD","description":null},{"id":30088308,"type":2,"amount":100000000,"new_amount":0,"bonus_amount":0,"bonus_total_amount":0,"currency":"USD","description":null},{"id":29686787,"type":2,"amount":100000000,"new_amount":0,"bonus_amount":0,"bonus_total_amount":0,"currency":"USD","description":null},{"id":12802418,"type":2,"amount":520000,"new_amount":0,"bonus_amount":0,"bonus_total_amount":0,"currency":"USD","description":null},{"id":12247374,"type":4,"amount":905880000,"new_amount":0,"bonus_amount":0,"bonus_total_amount":0,"currency":"USD","description":null}],"infeed":1,"confirmed_phones":["39 3450990971"],"need_phone_confirmation":false,"rate_in_one_click":true,"deposit_in_one_click":false,"kyc_confirmed":true,"kyc":{"status":3,"isRegulatedUser":true,"isProfileNeeded":true,"isPhoneNeeded":true,"isDocumentsNeeded":true,"isDocumentsDeclined":false,"isProfileFilled":true,"isPhoneFilled":true,"isDocumentsUploaded":true,"isPhoneConfirmationSkipped":false,"isPhoneConfirmed":true,"isDocumentsUploadSkipped":false,"isDocumentsApproved":true,"isDocumentPoiUploaded":true,"isDocumentPoaUploaded":true,"daysLeftToVerify":-1},"trade_restricted":false,"auth_two_factor":null,"deposit_count":38,"is_activated":true,"new_email":"","tc":false,"trial":false,"is_islamic":false,"socials":{"4":{"id":"10208062541311740","token":"CAAUMEkYTM0IBAMWBEvZBZBUfmfbujqPiXDbomiV2WS7JZBGFPeywcbZBtvyk4oZCQxO9Jqko87Vt3GT2Pt5dMbzKU7bMOj0C2zckMHq81DkAuZAUHEGULszSal1aYAXTPZCMQgGZBH3Pr8bZBm0xjXp1BZAXfdNoiJ6xOYvr2vkgt2En7L2l5zSaTr3UwPtviLg7YZD","group_member_reward":false}},"flag":"GB","cashback_level_info":{"enabled":false},"user_circle":"practiceRechargeFalse"}}
{"isSuccessful":true,"message":"","result":{"avatar":"http:\/\/graph.facebook.com\/10208062541311740\/picture?type=large","confirmation_required":0,"popup":[],"money":{"deposit":{"min":2,"max":1000000},"withdraw":{"min":2,"max":1000000}},"user_group":"VIP","welcome_splash":0,"functions":{"is_bonus_block":0,"is_trading_bonus_block":0,"is_vip_mode":0,"is_no_currency_change":0,"popup_ids":[""],"ext_fields":[]},"finance_state":"","balance":905.88,"bonus_wager":0,"bonus_total_wager":0,"balance_id":12247374,"balance_type":4,"messages":0,"id":7572160,"practice":0,"public":1,"group_id":3,"name":"Lorenzo Argentieri","nickname":null,"currency":"USD","currency_char":"$","mask":"$%s","city":"london","user_id":7572160,"first_name":"Lorenzo","last_name":"Argentieri","phone":"39 3450990971","email":"uni.lorenzo.a@gmail.com","created":1450694426,"last_visit":false,"site_id":1,"tz":"Europe\/London","locale":"it_IT","birthdate":639777600,"country_id":206,"currency_id":1,"gender":"male","address":"2G Doric Way","postal_index":"NW1 1LX","timediff":-7200,"tz_offset":60,"balances":[{"id":7780034,"type":1,"amount":9000000,"new_amount":9000000,"bonus_amount":0,"bonus_total_amount":0,"currency":"EUR","description":null},{"id":35924583,"type":2,"amount":240000,"new_amount":0,"bonus_amount":0,"bonus_total_amount":0,"currency":"USD","description":null},{"id":35924580,"type":2,"amount":80000000,"new_amount":0,"bonus_amount":0,"bonus_total_amount":0,"currency":"USD","description":null},{"id":21949793,"type":2,"amount":190000,"new_amount":0,"bonus_amount":0,"bonus_total_amount":0,"currency":"USD","description":null},{"id":30088308,"type":2,"amount":100000000,"new_amount":0,"bonus_amount":0,"bonus_total_amount":0,"currency":"USD","description":null},{"id":29686787,"type":2,"amount":100000000,"new_amount":0,"bonus_amount":0,"bonus_total_amount":0,"currency":"USD","description":null},{"id":12802418,"type":2,"amount":520000,"new_amount":0,"bonus_amount":0,"bonus_total_amount":0,"currency":"USD","description":null},{"id":12247374,"type":4,"amount":905880000,"new_amount":0,"bonus_amount":0,"bonus_total_amount":0,"currency":"USD","description":null}],"infeed":1,"confirmed_phones":["39 3450990971"],"need_phone_confirmation":false,"rate_in_one_click":true,"deposit_in_one_click":false,"kyc_confirmed":true,"kyc":{"status":3,"isRegulatedUser":true,"isProfileNeeded":true,"isPhoneNeeded":true,"isDocumentsNeeded":true,"isDocumentsDeclined":false,"isProfileFilled":true,"isPhoneFilled":true,"isDocumentsUploaded":true,"isPhoneConfirmationSkipped":false,"isPhoneConfirmed":true,"isDocumentsUploadSkipped":false,"isDocumentsApproved":true,"isDocumentPoiUploaded":true,"isDocumentPoaUploaded":true,"daysLeftToVerify":-1},"trade_restricted":false,"auth_two_factor":null,"deposit_count":38,"is_activated":true,"new_email":"","tc":false,"trial":false,"is_islamic":false,"socials":{"4":{"id":"10208062541311740","token":"CAAUMEkYTM0IBAMWBEvZBZBUfmfbujqPiXDbomiV2WS7JZBGFPeywcbZBtvyk4oZCQxO9Jqko87Vt3GT2Pt5dMbzKU7bMOj0C2zckMHq81DkAuZAUHEGULszSal1aYAXTPZCMQgGZBH3Pr8bZBm0xjXp1BZAXfdNoiJ6xOYvr2vkgt2En7L2l5zSaTr3UwPtviLg7YZD","group_member_reward":false}},"flag":"GB","cashback_level_info":{"enabled":false},"user_circle":"practiceRechargeFalse"}}