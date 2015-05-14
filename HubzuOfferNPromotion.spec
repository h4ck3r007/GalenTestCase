===========================================================
offerNPromotionModule		id		offerPromotions
offerNPromotionHeading		css		#offerPromotions .scheduler-border legend
offerNPromotionSubTitle		css		.subTit
offerNPromotionsPromo		id		promoCoverflow
offerNPromotionsPromoCurrentItem	css		#promoCoverflow .flip-current
offerNPromotionsPromoPrevItem	css		#promoCoverflow .flip-prev
offerNPromotionsPromoNextItem	css		#promoCoverflow .flip-next

==========================================================

offerNPromotionHeading
    text is: Offers & Promotions
    centered horizontally inside: offerNPromotionModule
    css font-size is: 32px
    css font-family contains: robotothin

offerNPromotionSubTitle
    text is: We have hand pick this properties for you!
    centered horizontally inside: offerNPromotionModule
    css font-size is: 12px
    css font-family contains: robotothin

offerNPromotionsPromo
    height: 390px
    width: 960px

offerNPromotionsPromoPrevItem
    aligned horizontally all: offerNPromotionsPromoNextItem

offerNPromotionsPromoCurrentItem
    aligned horizontally:offerNPromotionsPromoNextItem 70px 
