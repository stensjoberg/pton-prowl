import React, { Component } from 'react'
import Radium from 'radium'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';
import Day from './Day'

class Whenisgood extends Component {

  state = {
    weekdays: [],
  }

  weekdays = [
    {
      'day': 'monday',
      'timeblocks': [
        {'time': 8, 'avail': false},
        {'time': 9, 'avail': false},
        {'time': 10, 'avail': false},
        {'time': 11, 'avail': false},
        {'time': 12, 'avail': false},
        {'time': 13, 'avail': false},
        {'time': 14, 'avail': false},
        {'time': 15, 'avail': false},
        {'time': 16, 'avail': false},
        {'time': 17, 'avail': false},
        {'time': 18, 'avail': false},
        {'time': 19, 'avail': false},
        {'time': 20, 'avail': false},
        {'time': 21, 'avail': false},
        {'time': 22, 'avail': false},
        {'time': 23, 'avail': false},
        {'time': 0, 'avail': false},
        {'time': 1, 'avail': false},
        {'time': 2, 'avail': false},
        {'time': 3, 'avail': false},
      ]
    },
    {
      'day': 'tuesday',
      'timeblocks': [
        {'time': 8, 'avail': false},
        {'time': 9, 'avail': false},
        {'time': 10, 'avail': false},
        {'time': 11, 'avail': false},
        {'time': 12, 'avail': false},
        {'time': 13, 'avail': false},
        {'time': 14, 'avail': false},
        {'time': 15, 'avail': false},
        {'time': 16, 'avail': false},
        {'time': 17, 'avail': false},
        {'time': 18, 'avail': false},
        {'time': 19, 'avail': false},
        {'time': 20, 'avail': false},
        {'time': 21, 'avail': false},
        {'time': 22, 'avail': false},
        {'time': 23, 'avail': false},
        {'time': 0, 'avail': false},
        {'time': 1, 'avail': false},
        {'time': 2, 'avail': false},
        {'time': 3, 'avail': false},
      ]
    },
    {
      'day': 'wednesday',
      'timeblocks': [
        {'time': 8, 'avail': false},
        {'time': 9, 'avail': false},
        {'time': 10, 'avail': false},
        {'time': 11, 'avail': false},
        {'time': 12, 'avail': false},
        {'time': 13, 'avail': false},
        {'time': 14, 'avail': false},
        {'time': 15, 'avail': false},
        {'time': 16, 'avail': false},
        {'time': 17, 'avail': false},
        {'time': 18, 'avail': false},
        {'time': 19, 'avail': false},
        {'time': 20, 'avail': false},
        {'time': 21, 'avail': false},
        {'time': 22, 'avail': false},
        {'time': 23, 'avail': false},
        {'time': 0, 'avail': false},
        {'time': 1, 'avail': false},
        {'time': 2, 'avail': false},
        {'time': 3, 'avail': false},
      ]
    },
    {
      'day': 'thursday',
      'timeblocks': [
        {'time': 8, 'avail': false},
        {'time': 9, 'avail': false},
        {'time': 10, 'avail': false},
        {'time': 11, 'avail': false},
        {'time': 12, 'avail': false},
        {'time': 13, 'avail': false},
        {'time': 14, 'avail': false},
        {'time': 15, 'avail': false},
        {'time': 16, 'avail': false},
        {'time': 17, 'avail': false},
        {'time': 18, 'avail': false},
        {'time': 19, 'avail': false},
        {'time': 20, 'avail': false},
        {'time': 21, 'avail': false},
        {'time': 22, 'avail': false},
        {'time': 23, 'avail': false},
        {'time': 0, 'avail': false},
        {'time': 1, 'avail': false},
        {'time': 2, 'avail': false},
        {'time': 3, 'avail': false},
      ]
    },
    {
      'day': 'friday',
      'timeblocks': [
        {'time': 8, 'avail': false},
        {'time': 9, 'avail': false},
        {'time': 10, 'avail': false},
        {'time': 11, 'avail': false},
        {'time': 12, 'avail': false},
        {'time': 13, 'avail': false},
        {'time': 14, 'avail': false},
        {'time': 15, 'avail': false},
        {'time': 16, 'avail': false},
        {'time': 17, 'avail': false},
        {'time': 18, 'avail': false},
        {'time': 19, 'avail': false},
        {'time': 20, 'avail': false},
        {'time': 21, 'avail': false},
        {'time': 22, 'avail': false},
        {'time': 23, 'avail': false},
        {'time': 0, 'avail': false},
        {'time': 1, 'avail': false},
        {'time': 2, 'avail': false},
        {'time': 3, 'avail': false},
      ]
    },
    {
      'day': 'saturday',
      'timeblocks': [
        {'time': 8, 'avail': false},
        {'time': 9, 'avail': false},
        {'time': 10, 'avail': false},
        {'time': 11, 'avail': false},
        {'time': 12, 'avail': false},
        {'time': 13, 'avail': false},
        {'time': 14, 'avail': false},
        {'time': 15, 'avail': false},
        {'time': 16, 'avail': false},
        {'time': 17, 'avail': false},
        {'time': 18, 'avail': false},
        {'time': 19, 'avail': false},
        {'time': 20, 'avail': false},
        {'time': 21, 'avail': false},
        {'time': 22, 'avail': false},
        {'time': 23, 'avail': false},
        {'time': 0, 'avail': false},
        {'time': 1, 'avail': false},
        {'time': 2, 'avail': false},
        {'time': 3, 'avail': false},
      ]
    },
    {
      'day': 'sunday',
      'timeblocks': [
        {'time': 8, 'avail': false},
        {'time': 9, 'avail': false},
        {'time': 10, 'avail': false},
        {'time': 11, 'avail': false},
        {'time': 12, 'avail': false},
        {'time': 13, 'avail': false},
        {'time': 14, 'avail': false},
        {'time': 15, 'avail': false},
        {'time': 16, 'avail': false},
        {'time': 17, 'avail': false},
        {'time': 18, 'avail': false},
        {'time': 19, 'avail': false},
        {'time': 20, 'avail': false},
        {'time': 21, 'avail': false},
        {'time': 22, 'avail': false},
        {'time': 23, 'avail': false},
        {'time': 0, 'avail': false},
        {'time': 1, 'avail': false},
        {'time': 2, 'avail': false},
        {'time': 3, 'avail': false},
      ]
    },
  ]

  async componentDidMount() {
    try {
      const res = await fetch('http://0.0.0.0:8000/api/v1/users/root');
      const weekdays = await res.json();
      console.log("This weekdays : ")
      console.log(weekdays)
      this.setState({weekdays})
      console.log(this.state)
    } catch (e) {
      console.log(e);
    }
  }

    render() {
      return (
        <table>
          <tr>
            <th>
              {this.state.weekdays.map((item, i) => (
                <p>item.day</p>
            ))}
            </th>
          </tr>

          <tr>
            {this.state.weekdays.map((item, i) => (
              <p>item.timeblocks[0]</p>
            ))}
          </tr>



        </table>



      )
    }
}

export default Radium(Whenisgood)
