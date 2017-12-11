# sz42b without the p5 addon
def sz42(plaintext, key, lim = ""):
    # international telepgrah alphabet code
    # the index of each letter is its ITA2 code value
    ltrs = "iTrO_HNMnLRGIPCVEZDBSYFXAWJ<UQK>"
    figs = "i5r9_h,.n)4g80:=3+d?'6f/-2j<71(>"

    boolify = lambda x: list(map(lambda y: list(map(lambda c: bool(int(c)), y)), x))
    intify = lambda x: list(map(int, x))
    keylines = key.split('\n')
    chi =      boolify(keylines[:5])
    psi =      boolify(keylines[5:10])
    motor =    boolify(keylines[10:12])
    chiPos =   intify(keylines[12].split(' '))
    psiPos =   intify(keylines[13].split(' '))
    motorPos = intify(keylines[14].split(' '))

    output = []
    for letter in plaintext:
        # each of the chi and psi wheels operates on a single bit of the plaintext
        # for the sake of simplicity, treat the chi and psi wheels as 2 binary numbers
        chiCode = psiCode = 0
        for i in range(5):
            chiCode = (chiCode << 1) + chi[i][chiPos[i]]
            psiCode = (psiCode << 1) + psi[i][psiPos[i]]
        # get the ITA2 code of the current letter
        letterCode = ltrs.index(letter) if letter in ltrs else (figs.index(letter) if letter in figs else 0)
        # first XOR the letter with the chi wheels, then with the psi wheels
        encryptedLetter = letterCode ^ chiCode ^ psiCode

        # calculate the limitation
        basicMotor = motor[1][motorPos[1]]
        if lim == "chi2":   limitation = chi[1][(chiPos[1] - 1) % len(chi[1])]
        elif lim == "psi1": limitation = chi[1][(chiPos[1] - 1) % len(chi(1))] ^ psi[0][(psiPos[0] - 1) % len(psi[0])]
        else:               limitation = True
        totalMotor = basicMotor or not limitation

        # move chi wheels
        for i in range(5): chiPos[i] = (chiPos[i] + 1) % len(chi[i])

        # move the motor wheels
        # move motor 2
        if (motor[0][motorPos[0]]): motorPos[1] = (motorPos[1] + 1) % len(motor[1])
        # move motor 1
        motorPos[0] = (motorPos[0] + 1) % len(motor[0])

        # move the psi wheels
        if (totalMotor):
            for i in range(5): psiPos[i] = (psiPos[i] + 1) % len(psi[i])

        output += [encryptedLetter]

    shift = False
    cipherText = ''
    for code in output:
        if code == 31:   shift = False
        elif code == 27: shift = True
        if shift: cipherText += figs[code]
        else:     cipherText += ltrs[code]
    return cipherText

key1 = """00011110000110000101100100110101101011110
1100111011000101011000100001110
00111011001000011100110110011
00110010110010011001001111
01000101100100011101110
0010101010100100101101101010011011100111000
00101101010101010110011010010111100000111001011
101010101010100100110101011110000111000111011001001
10100110101010101011010000110011001101111101001000010
01010101011000101001110111101101000010001001101100110010101
1110101100110011000111101011011000110000111101100110001100001
1011101010101001010111010101010101010
0 6 7 3 4
8 26 16 21 24
20 10"""

text1 = "iWWVPXA<i/+9383-,d5)0(,3=>NHEZMXXX_YKCWV>EWPUACOMJJEnLVAIPRWCZSJZBrCOXNWVWDnVnV<)g_.d_f-/fj:-h-<220.n._ri=0++i(2:g0_j/+659h11f3>JF_RRTHUW_FMVJQnP>_LQBDYQA<h<>QNBHiZHPT>SCrHLDVJRPXUi_BXZ_UYLinV>VLM>RFBKXV_<041h,<:671?6//i<iii3.d,?dd./h':??95((')g-i7<(><jf(rnj,=,g_+2j-?02=:>H_TCQE>G>IP_iQIBAAnVGRCiGiXR_LPYLSB_JDWYCARinBT>XnTIEHSIQDDK_nJ>XNC>CH_FJKO_DWITCLOZMi><_<i/,+=<20i71in-+i6751n>JMDZ_W_UDQFRHJBO<r8r<,.g/>PT>ONNITVSKOQMVHKU>n>KTZEIEOHEZMVrW_YERiMnnZVJiKEVCWiGFKCU_MIB>CM<>CORPOONFnQEHYXGJiQRHXAnU_KQDD>PHXDDDUDL<?+=fnh8=.+9hr-gr-r19fnji+g.,24+'0)h57g'56,f'ni85+46r4(r_5.i82rn84h.3)g491.nh1_gd62d1-+ir__8-=7_i-0n64n)'>XniiKnOSEOQLHMGIUHIH<h():(6n?/3h63/6+ir0g,i9+:=_(r-j)(?4-d?02+r_+-9244=n.>JGDBOQTTVXOQM<-/66353+1958_:?9>IQYB<-?d(0r'g_),j>XWTnDMJGDTDnC>WEOGZrFMMUPOHnAAHHPXTKBCKTQSKTiNNUMRCHUHUXJIZ<j,4i-15,=.3)29n<<(.894:0f-5:>D_VVWO_QZ>CMGEQSGDPiDUJiTIUPXWC<h1+:=fi8ir5r><n2d-50f46.6-(/?(r.,31'_j+d732>RYWFVJDQ<ijrjf9g>ITFERrA<n<418598955<985=r:i_94==f>KiSJ>BHUG>MFPXK>DM<,463=j8,+j:+2>HJE_nVBWNZWEMZLXCLTYJ<+g)/2-ni-,j)jnr.9r24+h___)294<-?r-ng7:i/+ni,'/5.5dg6/:n26ndn-d63('+f</=96/9916(h40-f1n?>IGOiiGrVKLKQGIJNBYU_>rQBB<n0=/'(n9f>KPnXSRLLNPPIIDIrHQrBCMXAAQRLKETrZKInKiBKZG_P>_EEXiPFIOPQTQCZWVPAXWHHEYAMrTirnn>Xr>BOK<>ANEJYVUUAUJJrRUiXM<?r3f6:_8=./f3<0=5d93_hh5=?9>Br<5h::f1=g+7-?<_'h7=:in_201-945h<:._33,_d:2_i.+,_.._).08i9(=869d6h(fg56>FE>QUUOPiNYHiXBRQSZM<hn>JWKKUGRrDLFZPHAKBOnBGBDiQLVMHMWG_GMMGPQGVMi_EHBniFX_>XXDRNSXB_iHUMGrBDUKrEUCARS_FPHEKMSWC>RPHBBEYTOBSFRREFQYTMFOSPWEGETENWDENiGY<8/g'.0,3n:g256+=-467->nYC<d39<,>LCXGPE<72h237r.4g0=d+jg_.4(g8>ZBILET>QCnCiLXSWrTMZSTHKGRTFIVOGXPZiN<hrhj4fd/+=+>QYZSOGiYTALXEPrORrU_nPirSF_>U>JTJDAEZMMrKYDCTLnJJL_rRW<8i268/>VIOQIMUG>iSDVAWFYNZOXn_iZSGr<+>JUAMGXMiH_PWM<3=h7(+(1('69i5,:fi31_g9if52?jghi.(.nf9<h,/h+:dnhfj7'./nj.>F<f30653g6>PR_ILMKMDXATTUrOZMF<7>IQ>SJ_EPQRGODiC<>INHQL_IHrVPBVUCnHD<7::1-3f='>nKMJGTD<90/(1r43n<g+1?2-/0gg_==1_r7'29:/0g:jh6_.i>UFr>KSDF>_MGU<j7dif':1)11/.j>O_JQXZEZNVGXSHSBi>WJAU>iTTRrCQ>PDBiUnAEJHKYD_NJFLPFEPiWVL>VBSIDrENni>EGMMAM<2=h>TLNLNL_I_RJA<j2(i(74nn:>PiCPRiLAY<833i8.2(d67g-f_h->RJ>>iNI__MTiVVNFHFKiHXTD><r)24r.f9=),_2(8d(_(i5=(/9>OKBSJDRUAUYWMTJOZnNKPVFCVSG>VXRiBrrVWALQnAUMYDrJLFJBFSUiWrRCKP>RSJ>nWTGHEMRrCN_>UCnXiAQMTQCVVRREX_rODIKRZF<i)>NVHFIZUVTVF<.:<i.h=h6n-/f:.61'50=i3f2-_)>JDHN<j-ji_1-rih8,<0++7<>FVAZC>L_NHXDMBEINROIQJIV_ANACETXrUX_CULAnrKZSE<j0h06==-+7/=r'<d:=j4d3ggj-(<n/>KSIZTIMHVAiKPPIEOPIXSANZBOUEBEOWEXCQ_MWWISKBQGPMUBAAHO>L<72j1g>AJAUiOUiLRVEJSYZZY<)8i87-/==0hdr97:+3>_RSERBYQIiJXFKFAMWDMJDVFITHKrMCKWLZHWGAQrGrLXVnAiRPPKrZG<r8'_+i:??=rfi3:1</3(>E<-<)?+i0+(:979<.'(1:>P<f69617>_ESUiiSSCWF<7_/i/-,7,7)),34.=1f>_WXWKPNNPiN_CrPGJWAJrWUSEAYFQO_QOIGD_QUnFHQ>LUDAiCTKGMRA>Gn>ODOR>I>nYJHM<1_<6/_i+<'g,13<_79h4_n(,)+n_8-n'82n9)5(?j.>TWTJKVrZVPWXGIBHH>XFMH<29..n)d9jn+rhi,::24,/i)<hi)+0?+,'<3h4i7h7nrg5fh'7/988,6+j7<fijr58f/(5.'<57=7..(:d0/?==d+9j40=.-rj(71)-hng_67rh:).9:?=2d21'_?>GYTNR>IBKrrYSYPMYAHIGYFGrMRQ>CUOWXYJVDLLU_JMZDJVUAHUH>_UHBTEUSI_FUK>THXn>_XVPRVOJZHBUWEWJYUHQnRWJFIIAI<7'(hj32j=,2+'-<'(_37r'ff-23>MXJMDrYRTJKLXRLFWUGNKA>JQYIKE<n3n:?_gh<8i+j>>QKRDVWiUKLGEHR>rMIHBW>BFWJRAnVWI>BOXGHVPQTMGCFZUVQFnPSYiGM_W>rANADNB_OQrKKTBFEEDUAIAYiXiFCFLRQJ<',7i6j:?)=n.9)<>>GnZDiZASUJ_VUHBiWiCIQiAGKCPMXrARArViCNJrZSJIOPOW_VZ_ii>EiZRVAJFUiDNN>LGiMRXPTQNDNFSG>OU>VE_PNQDGJTFBrMBCNBUXUL<7.>ILERYBNIAXTDRIANA_UMiGKJIMFTIPNE<5nj/-0-5d?832'6rh+/2_=9<rg-93.4ng7'?_5,>RKMQA>AETHTiZ<8+?6//)+n-6=)4id.3638=+:5g=7?-7f1r(-=56:)5_5>DOTSnEB_POrrTPQURS>KS<><_57r.8)inh620fh(<64-6?j5d(h.i5h0246'i+_r9-3_04h.?h73:_),(_3(r30=0,>HVIFXQQZOGIGOnMYWPS<g9=:0-g/r?frhj36_?<9>rFiIMF<grf?.f8)n_?,76))?>JK>WrLABWGUWJQFUFiXLOUUnHTNTILM>Wr>OQPiirLSPWVOWPUWSJUUSGUUPLUXSFDDYHLJQBRMGZ_NLZQACYnniZnTMWnSAVrrVQZQQZKTTLLMZZIEXULZPBPiLY>>AWVUW>PB<_,:3fhr'5/'gd9f92>iGPMBHB>GHWLZJ_S<i8:<)hr2/)r?n=h5r7'6?-f<n.=:8?:>PLJEGHZ<:2:)25ji47h''+3r9(,0=g?6:2/'6i?501iiir,(f3,i1n,.=29''85/j9i0_rnfg7?-_.(r(g-/6//8f+=<=):(hr:':64_i:h2/'?/r(j.832/+r17f5+4i2d3_?6:nh-9?h<72fih9n912>XHPUiDJP_KNJIFAKLBTRANT_BnBMrOiMGiBMrFARG_SFODS_FNC_MSGFSK<d.(gf?0=4=g+8j<?/(),)f6?3_1hd/:./5-)97+d:0d8f64-n?=9h8/58hg+n66fr5i.n7fd)i1_5r>D<(3?(<r.i(=3'3(2infi72+f(41(>HX<h>CBT<))j77>FBrMQZUW>URFTiYX>WnU_DnEiHBRUSVGVQG<7=>HrJUPIEGEZrGFXHJVRGIN_T_V>iWEJBW<ihid'_fh:70.+_9699=67<>iTFCUENL>D<4?8:70')r+6+6i,)dnni3_((>LWLSKPVTOVYEY_TCiUM_JNKCRKHQQJCCXYLEDHDAGrQBKU_PrVYiV_ADBFSYTX<+3>KQCQLETnSGB_i>YBNMOUYRPZILTPJDBTDYODiOJXKIrKHNnNXrRNTBZCPCniDHNnBJVMiQD>VSi>V>VF>RrPDUVFri<r7'<nj+j/h//n11r?43j7?_2)j_9-).?>GAiLL<>GCOQHITHEDY<)?_i'081/((<_//572ng>iU>VBUSZKV>nIHnTBWNRL_<d8_=>XnXSAAJSTEVFYiNEUTJI_HGF_NMNrPTSYUSDTErZATPGFSnFM<i57i+7(<361.01=)0/.:0>rIOS<n=)-2<r5>TYVZNIFOOVHMMrDHOXWTTQWDHFDH__rZIROMUVWDVOCA<93)8)=8f+6i4)18/6n-73d9d9)+?'><)=)7-05(fir4?58(<,gr:/g(f>_P<67>AiSGNiTRBHYWFTX<9h<g079.j2+.3<h82/r1jg90'd7=-24,g5r)=9n>GMWROBOrOrVPZiPSFISLriTCMHFVZC>RTiiYFPZ<9n4.-5r10g:i5((7_':97r0i>SL_D_AZTnABYKJ>IZX_WnZNFRTFIVJRDiPYMAJONnAVPSWiFVHY<f83:+9-6+9)jr/6):3?--1i5h,0i')7gi)99.//?(j5-)j.j8'd0>WiT<1j+.i)>AP<>ADBrLUJGOTiMCKErrDIrJEUJnQWFSFNMYZJHYMP<:<12d:+.70n<9:2'4h+'jj.d05,j=579+0.f7>ULBOOZNQKKGDXiUrOCNVL_CXHUVUXWRNXVOUDMnZZW>VrKUTNHQXPHPiiDM>>IPC>GAS<(7f_g:52j'/r74>MiPCEBFT>TRI<i(r+hh-d85:?)ff6:-2r'065<<+7r?5'd>AnYMiZMAVV>P>ZEirQPOFinUQ>rWNAOrOKFSCWIM_<+f212:56)'>MVOP>>HiIQBN_>DiEAXGY>DIAEGnESEFZTEIPW<+1f//9+j2?=8)_8.6n9idi8)8,6:0ji0g(11/.26759.95.4d>CPHX<.rn5531'2:0:5>rU_iO<'i'd=rgi=f(g782jf8hj:h)3ff??>NSACKn_CMHVnOLJAYrTPCRD>QRLZCEWnMEXOUKSZDSOSDNQIO>r>Q_A>WNnTZrQFALEERPKS>YSKLn<92-:85.>KSLAUWRrFNWUMnFFFNBMWFY>PFJMFUNML_RTJGYOGASTIFV<_g-1?d?53+i-66:(?,92>>AUCONNUNLKinGJH_IVJ>CGOCVPA>WSFDVYBrQQiGJDVrNHSHZ<9:j3j<7h6f6='9j'034d(5g6i(<3n171/r=.:<3/h9rd8<,j5<90.irg4><17_fdr:+?/72'?4<g:_7)5r,5'6=+'0_dg>FELM_JrPNGZYWVrMIr<9n28'r9/d?2:>FKLW<>WKAAJYGEEVnnTOYXZiRPNVIKTUJHYiFniEUVNNJWI>MJCYXXTCJJHinFEFiMQWDGMHAnHrnJNX<_?7>GOCG>VKFnQK>P<hgd.===5=69).>Q_B>AHEMTOYTN>KERGMQrR>EiZUGiGZr>nrHUYM_DCXF<5,_=3()di95</+d'/1j).24fdi7_r=r?n45j+r)2>>iiiiiii"

print(sz42(text1, key1, "chi2"))

