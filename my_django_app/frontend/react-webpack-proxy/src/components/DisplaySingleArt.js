import React, { useState, useEffect } from 'react'
// import ReactDOM from 'react-dom'
import 'bulma'

const DisplaySingleArt = (props) => {
  const [art, setArt] = useState([])

  useEffect(() => {
    const id = props.match.params.id
    fetch(`/api/artwork/${id}`)
      .then(resp => resp.json())
      .then(resp => {
        console.log(resp)
        setArt(resp)
      })
  }, [])

  // useeffect for delete


  return <>
    {/* <h1>Hello World</h1> */}
    <section className="section">
      <div className="container">
        <div className="columns is-multiline">
          <div className="column is-one-third">
            <div className="card">
              <div className="card-content">
                <h2 className="subtitle">{art.name}</h2>

              </div>
              <div className="card-image">
                <figure className="card-image is-3by3">
                  <img src={art.image} className="art-image"></img>
                </figure>
              </div>
            </div>
          </div>
          <div className="column is-one-third">
            <div className="card 2">
              {/* <h3 className="subtitle">Artist: {art.artist}</h3> */}
              <h3 className="subtitle">Date Created: {art.created}</h3>
              <h3 className="subtitle">Location: {art.location}</h3>
              {/* <h3 className="subtitle">Art Period: {art.period}</h3> */}
            </div>
          </div>
        </div>
      </div>
    </section>
  </>
}

export default DisplaySingleArt