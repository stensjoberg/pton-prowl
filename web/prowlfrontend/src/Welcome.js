import React, { Component } from 'react'
import Radium from 'radium'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class Welcome extends Component {

  render() {
    return (
      <div id="bg">
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>

          <div id="center">
            <strong><p className="welc">Welcome to Prowl</p></strong>
            <p className="welc">Find study groups!</p>
            <br></br>
            <center><a href="/login">
              <button id="login">Log In</button>
            </a></center>
        </div>
      </div>
    )
  }
}

export default Radium(Welcome)
