import React, { Component } from 'react'
import Radium from 'radium'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class Whenisgood extends Component {

  state = {
    weekdays: [],
  };

  weekdays = [
    {
      'day': 'monday',
      'timeblocks': [
        {'time': 8, 'avail': false},
        /*{9, false},
        {10, false},
        {11, false},
        {12, false},
        {13, false},
        {14, false},
        {15, false},
        {16, false},
        {17, false},
        {18, false},
        {19, false},
        {20, false},
        {21, false},
        {22, false},
        {23, false},
        {0, false},
        {1, false},
        {2, false},
        {3, false},*/
      ]
    }
  ]

  componentDidMount() {
    this.setState(this.weekdays)
  }

    render() {
      return <p>Hello world</p>
    }
}

export default Radium(Whenisgood)
