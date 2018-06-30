import React, { Component } from 'react'
import Radium from 'radium'
import { styles } from './styles'
import './css/normalize.css';
import './css/skeleton.css';
import './css/stylesheet.css';


class Button extends Component {
  render() {
    return (
      <button class="button" style={Object.assign({},

      )}>
        {this.props.children}
      </button>
    );
  }
}

export default Radium(Button);
