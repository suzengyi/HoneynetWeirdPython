# coding=utf-8

from http.server import HTTPServer, BaseHTTPRequestHandler

import binascii


class TestHTTPHandle(BaseHTTPRequestHandler):
    def do_GET(self):
        buf = binascii.a2b_hex(
            "00ed3129559e691a601e3c23f6e16e4f031c3c23f6a16e4f036d2123f6e10a4f037a3d239ae16e15031e5923f68b6f4f671c3ca0f7e16f2b021e6f0bf5e16e4f6ae1c3dc09af1d06031e3c2efc850b2d76795b4684c10a2a777b5f5793854042096d554498801a3a717b0603c4d25d2930780f41c1d0587b352a0e40c4d55c7b352b0e40c4d6587b302f0b11c580592b332c0d46dee36e4f036a3f23f6e11d36706a3823f6e10b376a6a1423f6e16e67031e3c23dee16e4f036d2e23f6e11b3b6a724f0c9080052a5c7d534793cf1e3677163c23f6dd0320676b5046c8e26e4f036d3823f6e1624e051f3c23f6e16e4f031e3c26f6e16e0f031e3c5023e16e4f98e0c1bb0c1bfbb7f4b2c9d761139fdbedf0bdce1d5186a780f8d9a31403e3addc9ae3ff4939b7cdd7c88df42569bb9fa8d4f16b3d2bfd82c4bdfce7b623afd5baa0e89f4d01d0f7ccfd89f24d53bbfaac33908f191680e7feb199e3554395e59cf88fbf0871f7b39288c2b765007ddfe99ab1ca7a6b8dcc841bb9a71e65efbded6024538dfe1137f769490d8f936e5b6c2734459dee00270171597be4d60f78384761fbadbb6d1a542c617721b33f4542501566bd2f27071e577902a5a34b053c4b031fbf0a57123b288a17c5d2317f2c54100f8ec9654f031e55dc091e91016a1b3c23f6885fdc021e5f23f6e16e4f031e3c21f6e16e0f031e3c50ebe16e4f671e3c47f7e1024f03443c2393e16e25021e5821f6626f4f027a3d23a5c96d4f031e55dc091e910170573c23f6ec642b667c494491841c6f677b484695950b2b2d1336509f86002e776b4e46ccc15c7c30780f45c583597e352a0a17c4825c7b312a0a16c4825c78352a0f12c1d35d2e347a0c11c784464d031e3c57f5e16e4f70674f57f2e16e4f66665557dee16e4f03363c23f6e1464f031e3c50e4e16e4f766a554f85ce082e687b634099850b617367482bf6e16e736e7158569a84504c031e3c50f2e16e4f0f1f3a22f6e16e4f031f3c23f6e26e4f037d3c23f692424f031e1253a2c63c1e275072edbbaa605b5c590766b2d62e0e3f21020dbedb54605f280a0094d32d733366760eda99464d031e3c6d9fe16f4f03363f23f6e11a4a031e3c7eb9a22501771f3c23f6a41a4e031e3c6fdee06e4f036a3d23f6e12f67031e3c23dee16e4f036d2923f6e17f5f624f6675b8b82b1c6a5a6e68abbe200500426e57f3e16e4f735e6462aee66e4f036d3823f6e140633c345523f7e16e26031e3c2395e16e4f031e3c23f6e36e4f035e3c23f692734f031e5823f6856f4f6f1e3c79f6e10b4f03743d2392e36ecc021e3d47f7e13d67001e3c239f1e91b0fc504f6af6e16e42097a59418386092a713e584682840d3b667a122efc9207286d7f48568484546f312d0f45c5875d2d342f0a17c0d55c2c312a0e17c0d45c2c31290a17c5d0597d307f0b47c6d35f2a2b1c3c23f6956d4f031e4f5a85956a4f031e595b9f95464f031e3c0bf6e16e4f2b1e3c23f6927c4f031e49579f8d1d60657f5746a982012b66304c5a82e96e4f0322514c9294022a3d1d3c23f6926a4f031e3022f0e06e4e031e3c22f6e16e4c031e3c60f6e16e3c141e3c23d3a0511b3e22631bcf5d59794a2a0f5544d041e22f32440bf5e16e4f4d6a3c23f6e10d4f031e3c23f6e16e4d031e3c63f6e16e3c1e1e3c2392e16e2b021e5023f6bb6e4f661e3c49f7e10a4d039d3d23f7856f4f50363f23f6e107b0fce1c36d85a86e4f0313364793831b28647b4e0392841a2a606a5947d8ec643c6a79524282941c2a393e0e10c5875d29307c0b12c0d5587b317d0e17c4d5587a317d0e14c0d55d7e342c0f42c1855e7d327b1421f6e16e3b001e3c2385981d3b071e3c239399073b2b1e3c23f6c96e4f031e1423f6e16e3c111e3c238395072370315a429d84312c6c7a590d86981a47031e3c1f9b8e0a3a6f7b0220f6e16e3c071e3c23fae0684e031f3c23f6e36e4f031b3c23f6926e4f036d1923f6e15d014e0f6c69c2a8297d465a0b60b7d553714223079aced940fa372a5910"
            "b6d241052e32440bf7e16e4f4d363f23f6e11a4c031e3c6db2b81a4b031e3c7eaeaf363b001e3c23b4bf2167011e3c2382e36e4f031c2757f7e16e4f50363c23f6e1464f031e3c50e3e16e4f120e5d72acb72016464d5567a4aa33104d543f7fa492674f031e3376a2bf24195e402937f6e16e3c011e3c23dcca464e031e3c57f2e16e4f475c7966dee06e4f036a3823f6e1340757411423f6e16e67031e3c2385f46e4f030f2c42a7bb38015a5b6f4ab2b325125c507620aab31a4c031e3c6bb4a97d4f031e4f21f6e16e63297d3c23f6e16e4f031e3e23f6e12e4f031e4f3ef6e16e2b031e5822f68d6e4f591e3c46f6e1044e037a3e2375e06e4e671f3c70dee26e4f0377c3dc091e203c4a1e3c23fbeb0a2a616b5b4493934e2b666a594082840a610e144f4a918f0f3b766c5919d6d35d7c652d5a1094d65f793728081195d35a7d3728091195d35979372d0d14c4d20f78672e0e1293c96c4f031e4820f6e16e3c7a6d4827f6e16e2a7b77480bf6e16e4f2b1e3c23f6c96e4f031e4f31f6e16e3a77775050d9870f2466415f4c9284403f7a6a3423f6e152226c7a494f93df6d4f031e4f27f6e16e4302183d23f7e16e4f041e3c23f0e16e4f401e3c23855a6e4f038fd8c069018ee4dcc38afa2c4cb598b1cae88c2430da82cdcc73e83daba788b8d9f89c3420c4f4bdc78398cf59d685b6abfc954424d8e0d1b390ec584845eaa5d19f80d740ce539c83ddbb6c01c8d8e183a8da6d709ac58df9baa8006ae64b849bc4a37409ef301965403c8b9820bb766b355484e4162007785034988885296511544017800e6d5843371689b8326c5d4b027da4db34003fe27069c1ae260921537827c8a62e3775470918b1dd5616342b506cc1d019284933105bdeeb6e4f03506e22f6e16e263be1c3dc82e76e4f034c727ebefb713b011e3c23a8a81d66031e3c18d0c44e3a627c1e01d2c24725223a15059acf5c171250757aa1b122275d426f78b7b33112480c6b7585986e4f03f0f1f83f129cb3b0b0888a4e5eb5bbf4e4c0c6091d88f9afdcd8de1b0ac887e6fe9eed25be48124e55196bbec92a13572c3e22eaeb57470d3e3f3eb1b33b1d494e6862bef5784612094a5ac2df537f770a0b11cdc109220c3d0405d3c3073e77734e4c84ec61461114372fee85391c565f673df3fd774c1c034f29f6e16e2e43497f3e98a8260d5c6d3523f6e1082f7e6b617fb4bf7f3c011e3c23f7fb4641031e3c57f2e16e4f7941656d82e76e4f035b6161b7a4273b0a1e3c23b0a1331a42537e6bb8956a4f031e7667b9be1a49031e3c76b7ac2c074d4c3123f6e11a4b031e3c62aba82b3b071e3c23aaa9230077193c23f6a52c0c415a723a82e66e4f037d697dada9311077183c23f6b72e1343536357f1e16e4f475c7f62aba82b3b041e3c23a0b4350241567257fee16e4f647d4049aabe2d162b193c23f695664f031e687baaab2e034250482ef6e16e0c5d447a4fb3b12d3f4556626d82e46e4f0341737cbba71a4b031e3c69bab9243b001e3c23a9a8343b071e3c23bba32601771f3c23f6af464f031e3c0bf6e16e4f700b3c23f6f07e2e52446a6dafa43d26474c777ea9af244c5f4c4829f6e16e1e484a647f86a92a0f4d083c23f692764f031e7e60b0dc5c732f27091bd5d45b7b122c1713d4cf496325375f23f6e16e4f031e3c21f6e16e0f031e3c50ebe16e4f671e3c47f7e1024f03443c2393e16e25021e5821f6626f4f027a3d23a5c96d4f031e55dc091e910170573c23f6ec642b667c494491841c6f677b484695950b2b2d1336509f86002e776b4e46ccc15c7c30780f45c583597e352a0a17c4825c7b312a0a16c4825c78352a0f12c1d35d2e347a0c11c784464d031e3c57f5e16e4f70674f57f2e16e4f66665557dee16e4f03363c23f6e1464f031e3c50e4e16e4f766a554f85ce082e687b634099850b617367482bf6e16e736e7158569a84504c031e3c50f2e16e4f0f1f3a22f6e16e4f031d3c23f6e86e4f031d3c23f692fc4f031ef8134c2cd6f8dfaa88e44450b4e2"
            "add993883849c69ca5bbf28454574dd19d00a1b8282591d8c988a8cd647083c18deeb2a8043de6b4879bfcfd396067307d1745580b98165e746b2c5284161e200970502c9888622d651f5e40f0870e77584324fbadb8b51955395170d0b63e744d531a6abcc22108395b78e8b4a0ad723da00118cda96f7844120847b5f35e374933105bdee96e4f03504822f6e16e1a601e3c23f6e16e4f031c3c23f6a16e4f036d2123f6e10a4f037a3d239ae16e15031e5923f68b6f4f671c3ca0f7e16f2b021e6f0bf5e16e4f6ae1c3dc09af1d06031e3c2efc850b2d76795b4684c10a2a777b5f5793854042096d554498801a3a717b0603c4d25d2930780f41c1d0587b352a0e40c4d55c7b352b0e40c4d6587b302f0b11c580592b332c0d46dee36e4f036a3f23f6e11d36706a3823f6e10b376a6a1423f6e16e67031e3c23dee16e4f036d2e23f6e11b3b6a724f0c9080052a5c7d534793cf1e3677163c23f6dd0320676b5046c8e26e4f036d3823f6e1624e051f3c22f6e16e4d031e3c20f6e16e7c031e3c50e8e16e4f37597a3ba6a2510f43a9021ea0da540a3a298917c2845d0f3031760eda99464e031e3c6ddee06e4f036a3423f6e1391057426567aea2464d031e3c71ffe16e4f771d3c23f6a93a102b1f3c23f6956f4f031e710bf6e16e4f700b3c23f6f07e2e52446a6dafa43d26474c777ea9af244c5f4c4f2af6e16e40564a6269a0bc305a2f1e3c2385e36e4f03341750f2e16e4f0343746e85e56e4f031e7560be926b4f031e3d69b4ae3d3c071e3c23f6b42e17701b3c23f6e0380e5c4d142bf6e16e3b011e3c23b5b91a4b031e3c7abaa12e3b071e3c23a8ad360c77143c23f6b0250d53407778a8a8373b001e3c23a8a8353b001e3c23baa33c1d271e3c23a4ea6e4f03363f23f6e11a4b031e3c7fb4a2313b071e3c23bca53017771b3c23f6a8290e4a461423f6e16e67021e3c23a4c96e4f036d2923f6e17f5f624f6675b8b82b1c6a5a6e68abbe200500426e57f5e16e4f5c47790af6e16e3c0b1e3c23c4d16c6120323b0982e96e4f0373527eb8a62d3c77362d23f6e13c66031e3c71e1e16e4f510f3c23f6b36c4f031e6e22f6e16e1d071e3c2382e56e4f035e6462aeb3694f031e6e23f6e16e3b021e3c23b4b3644f031e4825f6e16e094d5c646aae956a4f031e7c6ba2be3c42031e3c71d2e16e4f512c3c23f695664f031e514da8af2d07706a1423f6e16e67031e3c23dee16e4f036d2923f6e17f5f624f6675b8b82b1c6a5a6e68abbe200500426e57fee16e4f0d426368ada0275a021e3c2385c36e4f035e7665bea52b0f475c7e68b3a850773f31061fcef8586937240d18c4d85268283e16")
        self.protocal_version = "HTTP/1.1"
        self.server_version = 'nginx/1.4.6 (Ubuntu)'
        self.send_response(200)
        self.send_header("Content-Type", "probably/nonsense")
        self.end_headers()
        self.wfile.write(buf)
    def do_POST(self):
        pass

http_server = HTTPServer(('0.0.0.0', 80), TestHTTPHandle)
http_server.server_name = 'ninja-game.org'
print(http_server.server_name)
http_server.serve_forever()  # 设置一直监听并接收请求
