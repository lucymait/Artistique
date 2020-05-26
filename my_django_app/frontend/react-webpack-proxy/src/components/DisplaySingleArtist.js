import React, { useState, useEffect } from 'react'
// import ReactDOM from 'react-dom'
import 'bulma'

const DisplaySingleArt = (props) => {
  const [artist, setArtist] = useState([])

  useEffect(() => {
    const id = props.match.params.id
    fetch(`/api/artwork/artist${id}`)
      .then(resp => resp.json())
      .then(resp => {
        console.log(resp)
        setArtist(resp)
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
                <h2 className="subtitle">{artist.name}</h2>
              </div>
              <div className="card-image">
                <figure className="card-image is-3by3">
                  <img src={artist.image} className="art-image"></img>
                </figure>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </>
}

export default DisplaySingleArt