.. route-map documentation master file, created by
   sphinx-quickstart on Sat Dec 20 23:11:46 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

route-map documentation
=======================


全国の鉄道路線図 

.. raw:: html

   <style>
   @charset "utf-8";


   #mapsvg {
    background-image: url(../tetsudo-rd2025/map_text.png);
    background-repeat: no-repeat;
    background-size: 55%;
    flex: 1;
    margin-right: 5%;
   }
   #mapsvg svg {
    width: 100%;
    height: auto;
   }
   .region {
    flex: 1;
   }
   #map li {
    list-style: none;
   }
   .region li {
    margin-bottom: 0.3rem;
   }
   .region a {
    display: block;
    padding: 0.6rem 2rem 0.6rem 1rem;
    text-align: left;
    color: #fff;
    font-weight: 500;
    font-size: 1.3rem;
    line-height: 120%;
    border-radius: 5px;
    background-color: #175373;
   }
   .region .sub_region {
    display: flex;
    justify-content: center;
    align-content: space-between;
    margin-left: 0.6rem;
    margin-top: 0.3rem;
   }
   .region .sub_region li {
    flex: 1;
    margin-left: 0.4rem;
    margin-bottom: 0;
   }
   .region .sub_region a {
    font-size: 1rem;
    height: 100%;
    background-color: #8899ad;
   }

   h3 span#contents::after {
      content:"";
      background-color:#ddd;
   }

   h4 {
      margin:2% auto 2%;
      padding:1rem 0;
      text-align:center;
      max-width:80%;
   }
   .note {
      background-color:#000;
      border:1px solid #000;
      color:#fff;
   }

   .note h4 {
      padding:0;
   }
   .rcopy {
      font-size:0.85em;
      text-align:center;
      margin-bottom:3%;
   }
   .shoei {
      text-align: center;
   }


   /*鉄軌道路線図ここから*/
   #map .flex_container {
      width:80%;
      margin:5% auto;
   }

   #mapsvg {
      background-image:url('../tetsudo-rd2025/map_text.png');
      background-repeat:no-repeat;
      background-size:55%;
      flex:1;
      margin-right:5%;
   }

   #mapsvg svg {
      width:100%;
      height:auto;
   }

   #mapsvg .hokkaido {
      fill:#7ac8f3;
   }

   #mapsvg .tohoku {
      fill:#8183c5;
   }

   #mapsvg .kantokoshinetsu {
      fill:#ec7aab;
   }

   #mapsvg .kinkichubu {
      fill:#fad181;
   }

   #mapsvg .chugokushikoku {
      fill:#d3e179;
   }

   #mapsvg .kyushu {
      fill:#92c897;
   }

   #mapsvg text {
      fill:#175373;
      font-size:1.5rem;
      font-weight:500;
      opacity:0;
      transition:0.3s;
   }

   #mapsvg a:hover + text {
      opacity:1.0;
   }

   .region {
      flex:1;
   }

   .region li {
      margin-bottom:0.3rem;
   }

   .region a {
      display:block;
      padding:0.6rem 2rem 0.6rem 1rem;
      text-align:left;
      color:#fff;
      font-weight:500;
      font-size:1.3rem;
      line-height:120%;
      border-radius:5px;
      background-color:#175373;
   }

   .region a::after {
      content:"";
      display:inline-block;
      width:1.2em;
      height:1em;
      position:absolute;
      top:50%;
      right:0.8rem;
      transform:translate(0,-0.5em);
      background-image:url("../img/arrow.svg");
      background-size:contain;
      background-repeat:no-repeat;
   }

   .region a.hokkaido:hover {
      background-color:#7ac8f3;
   }
   .region a.tohoku:hover {
      background-color:#8183c5;
   }
   .region a.kantokoshinetsu:hover {
      background-color:#ec7aab;
   }
   .region a.kinkichubu:hover {
      background-color:#fad181;
   }
   .region a.chugokushikoku:hover {
      background-color:#d3e179;
   }
   .region a.kyusyu:hover {
      background-color:#92c897;
   }

   .region a:hover {
      text-decoration:none;
   }

   .region .sub_region {
      display:flex;
      justify-content: center;
      align-content:space-between;
      margin-left:0.6rem;
      margin-top:0.3rem;
   }

   .region .sub_region li {
      flex:1;
      margin-left:0.4rem;
      margin-bottom:0;
   }

   .region .sub_region a {
      font-size:1rem;
      height:100%;
      background-color:#8899ad;
   }

   /*鉄軌道路線図ここまで*/


   /*資料編アーカイブここから*/
   #documents {
      flex:1;
      margin-right:5%;
   }

   #documents h4 img {
      max-height:7rem;
      width:auto;
   }

   /*資料編アーカイブここまで*/


   /*車両図鑑ここから*/
   #dictionary {
      flex:1;
   }

   #dictionary h4 img {
      max-height:7rem;
      width:auto;
   }

   #dictionary .title-kankou{
      position: absolute;
      right: -10px;
      top: -40px;
   }

   .flex_container {
    display: flex;
    justify-content: center;
    align-content: space-between;
    flex-wrap: wrap;
   }
   
   /*車両図鑑ここまで*/

   #link {
      margin-bottom:0;
      background-color:#004b74;
      background-image:none;
      color:#fff;
      border-bottom:1px solid #eee;
   }

   #link img {
      border:1px solid #fff;
   }

   #twitter {
      margin-bottom:0;
      background-color:#c1e5f6;
   }

   /*レスポンシブ用設定*/
   @media screen and (max-width:890px) {
      #map .flex_container {
         width:90%;
      }
      
      #documents h4 img,
      #dictionary h4 img {
         height:auto;
      }

   }

   @media screen and (max-width:767px) {
      h4 {
         max-width:100%;
      }
      
      #intro p {
         width:90%;
      }
      
      .box {
         width: 95%;
      }

      #intro .entry a {
         font-size:1.25rem;
         line-height:1.4em;
      }
      
      #mapsvg {
         margin-right:0;
         margin-bottom:5%;
      }

      #documents {
         margin-right:0;
      }
   }

   body {
      font-family:'Noto Sans JP', 'Hiragino Kaku Gothic ProN', 'ヒラギノ角ゴ ProN W3', Meiryo, メイリオ, Osaka, 'MS PGothic', arial, helvetica, sans-serif;
      font-size:20px;
      line-height:120%;
      background-color:#eee;/*ボディーの背景色*/
      -webkit-text-size-adjust:100%;
      width:100%;
      height:100%;
   }

   * a {
      transition:all 0.2s ease;
      -webkit-trantision:all 0.2s ease;
   }

   * a:hover {
      opacity:0.8;
      text-decoration:underline;
   }

   * a.nolink {
      pointer-events: none;
   }

   li {
      list-style:none;
   }

   a,
   label {
      cursor:pointer;
   }

   img {
      max-width:100%;
   }

   /*レスポンシブ用設定*/
   @media screen and (max-width:767px) {
      img {
         max-width:90%;
         display:block;
         margin:auto;
      }
   }

   </style>
   <section id="map">
   <div class="flex_container">
      <div id="mapsvg">
        <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 432 429.9" width="432" height="429.9">
          <g>
            <rect x="111.6" y="365.4" width="61.2" height="33.7" fill="#eee"></rect>
            <rect x="96.3" y="297.3" width="91.8" height="61.2" fill="#eee"></rect>
            <rect x="195.3" y="297.3" width="96.9" height="102" fill="#eee"></rect>
            <polygon points="432,7.5 299.4,7.5 299.4,140.1 340.2,140.1 340.2,118.5 432,118.5" fill="#eee"></polygon>
            <polygon points="299.4,147.3 299.4,239.1 340.2,239.1 340.2,290.1 401.4,290.1 401.4,147.3" fill="#eee"></polygon>
            <polygon points="332.5,246.3 299.4,246.3 299.4,399.3 401.4,399.3 401.4,297.3 332.5,297.3" fill="#eee"></polygon>
            <rect x="7.5" y="297.3" width="81.6" height="132.6" fill="#eee"></rect>
          </g>
          <a xlink:href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［北海道地方］.html"><polygon class="hokkaido" points="424.5,0 291.9,0 291.9,132.6 332.7,132.6 332.7,111 424.5,111 "></polygon></a>
          <text x="20" y="150">北海道地方</text>
          <a xlink:href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［東北地方］.html"><polygon class="tohoku" points="291.9,139.8 291.9,231.6 332.7,231.6 332.7,282.6 393.9,282.6 393.9,139.8 "></polygon></a>
          <text x="20" y="150">東北地方</text>
          <a xlink:href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［関東・甲信越地方］.html"><polygon class="kantokoshinetsu" points="325,238.8 291.9,238.8 291.9,391.8 393.9,391.8 393.9,289.8 325,289.8 "></polygon></a>
          <text x="20" y="150">関東・甲信越地方</text>
          <a xlink:href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［近畿・中部地方］.html"><rect class="kinkichubu" x="187.8" y="289.8" width="96.9" height="102"></rect></a>
          <text x="20" y="150">近畿・中部地方</text>
          <a xlink:href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［中国・四国地方］.html">
            <g>
              <rect class="chugokushikoku" x="104.1" y="357.9" width="61.2" height="33.7"></rect>
              <rect class="chugokushikoku" x="88.8" y="289.8" width="91.8" height="61.2"></rect>
            </g>
          </a>
          <text x="20" y="150">中国・四国地方</text>
          <a xlink:href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［九州地方］.html"><rect class="kyushu" x="0" y="289.8" width="81.6" height="132.6"></rect></a>
          <text x="20" y="150">九州地方</text>
        </svg>          
      </div>
      <ul class="region">
        <li><a href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［北海道地方］.html" class="hokkaido">北海道地方</a></li>
        <li><a href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［東北地方］.html" class="tohoku">東北地方</a></li>
        <li><a href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［関東・甲信越地方］.html" class="kantokoshinetsu">関東・甲信越地方</a>
        <ul class="sub_region">
          <li><a href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［東京近郊］.html">東京近郊</a></li>
          <li><a href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［都心部地下鉄］.html">都心部地下鉄</a></li>
        </ul></li>
        <li><a href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［近畿・中部地方］.html" class="kinkichubu">近畿・中部地方</a>
        <ul class="sub_region">
          <li><a href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［京阪神近郊］.html">京阪神近郊</a></li>
          <li><a href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［名古屋近郊］.html">名古屋近郊</a></li>
        </ul>
        <ul class="sub_region">
          <li><a href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［大阪・名古屋地下鉄］.html">大阪・名古屋地下鉄</a></li>
        </ul></li>
        <li><a href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［中国・四国地方］.html" class="chugokushikoku">中国・四国地方</a></li>
        <li><a href="../tetsudo-rd2025/鉄道手帳WEB｜全国鉄軌道路線図2024-2025［九州地方］.html" class="kyusyu">九州地方</a></li>
      </ul>
      </div></section>
.. end HTML


.. toctree::
   :maxdepth: 2

   ROUTE/Shinkansen/index
   ROUTE/JRE/index
   ROUTE/TokyoMetro/index
   ROUTE/Toei/index
   ROUTE/Tokyu/index
