<!DOCTYPE html>
<html>
  <head>
    <title>Web based data query system!</title>

    <style type="text/css">
        div.left {
        position: relative;
        width: 700px;
        height: 200px;

        }

        div.right {
            position: relative;
            width: 400px;
            height: 200px;

        }


      body {
      font-family:sans-serif;
      color:#4f494f;
      background-color: #E0F7FE;}
      form input {border-radius: 7.5px;}
      h5 {display: inline;}
      .label {text-align: right}
      .guestbook {float:left; padding-top: 10px;}
      .name {width:100%;float:left; padding:3px;}
      .wrapper { padding-left: 25px; padding-top: 20px}
    </style>
  </head>

  <body>

    <div class="wrapper">
        <h1 align="center">FindAPIs : A web based data query system!</h1>

      <div class = "left" id="api" style="width: 200; height: 100%;
      text-align: left;
      vertical-align: top; float: left;">
      <h2>Search APIs with filters!</h2>
      <form method="post" class="form" action="/search1api" method='post'>

        <table >

          <tr>
            <td>year
            <select id="year_opt" name="year_opt">
              <option value="1">=</option>
              <option value="2">></option>
              <option value="3"><</option>
            </select>
            </td>
            <td><input type="text" name="year"/></td>
          </tr>
          <tr>
            <td>protocols</td>
            <td><input type="text" name="protocols"/></td>
          </tr>
          <tr>
            <td>category</td>
            <td> <input type="text" name="category"/></td>
          </tr>
          <tr>
            <td>rating
            <select id="rating_opt" name="rating_opt">
              <option value="1">=</option>
              <option value="2">></option>
              <option value="3"><</option>
            </select>
            </td>
            <td><input type="text" name="rating"/></td>
          </tr>
          <tr>
            <td>tags</td>
            <td>  <input type="text" name="tags"/></td>
          </tr>
          <tr>
            <td>keywords</td>
            <td><input type="text" name="keywords"/></td>
          </tr>
        </table>
        <input type="submit" value='Search!'/>
        <h3>Results:</h3>
        %for name in mynames1:
        <div class="name">
        <h5></h5>  {{name['title']}},
        </div>
        %end
      </form>
    </div>

    </div>
    <div class = "right" id="mash" style="width: 400; height: 100%;
    text-align: left;
      vertical-align: top; float: left;">
      <h2>Search mashUps's with filters!</h2>
      <form method="post" class="form" action="/search1mash" method='post'>

        <table >

          <tr>
            <td>year
            <select id="year_opt" name="year_opt">
              <option value="1">=</option>
              <option value="2">></option>
              <option value="3"><</option>
            </select>
            </td>
            <td><input type="text" name="year"/></td>
          </tr>
          <tr>
            <td>APIs</td>
            <td><input type="text" name="APIs"/></td>
          </tr>
         <tr>
            <td>tags</td>
            <td><input type="text" name="tags"/></td>
          </tr><tr>
            <td>keywords</td>
            <td><input type="text" name="keywords"/></td>
          </tr>

          <tr>  </tr>
          <tr>  </tr>
        </table>
        <input type="submit" value='Search!'/>
        <h3>Results:</h3>
        %for name in mynames1:
        <div class="name">
        <h5></h5>  {{name['title']}},
        </div>
        %end
      </form>
    </div>
    </div>
    <div class="wrapper">


  </body>
</html>