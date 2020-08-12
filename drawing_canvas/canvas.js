window.addEventListener('load', () => {
    const canvas = document.querySelector('#canvas')
    const ctx = canvas.getContext('2d')
    const popSquare = document.querySelector('#popSquare')
    const popNotSquare = document.querySelector('#popNotSquare')
    const saveButton = document.querySelector('#save')

    var square, notSquare , data, timer
    var notSquareData = {"data":[]}
    var squareData = {"data":[]}


    canvas.height = window.innerHeight/2;
    canvas.width = window.innerWidth/2;

    let painting = false;

    function startPosition(e) {
        timer = new Date().getTime();
        data = []
        painting = true;
        draw(e)
    }

    function endPosition(){
        console.log(data)
        square = document.getElementById('square')
        notSquare = document.getElementById('not-square')
        painting = false;
        ctx.beginPath();
        if (square.checked) {
            squareData["data"].push(data)
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }
        else if (notSquare.checked){
            notSquareData["data"].push(data)
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }
        else{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }
        document.getElementById('squareCounter').innerHTML = squareData.data.length
        document.getElementById('notSquareCounter').innerHTML = notSquareData.data.length
    }

    function draw(e){
        time = new Date().getTime() - timer

        if(!painting) return;
        ctx.lineWidth = 10;
        ctx.lineCap = "round";

        data.push([time,e.clientX,e.clientY])

        ctx.lineTo(e.clientX, e.clientY)
        ctx.stroke()
    }

    function ps(){
        console.log(squareData)
        if (squareData.data.length > 0) squareData.data.pop()
        document.getElementById('squareCounter').innerHTML = squareData.data.length
    }

    function pns(){
        if (notSquareData.data.length > 0) notSquareData.data.pop()
        document.getElementById('notSquareCounter').innerHTML = notSquareData.data.length
    }

    function saveData() {
        var squareBlob = new Blob([JSON.stringify(squareData)],
            { type: "application/json" });
        saveAs(squareBlob, "square.txt");
        var notSquareBlob = new Blob([JSON.stringify(notSquareData)],
            { type: "application/json" });
        saveAs(notSquareBlob, "notSquare.txt");
    }

    canvas.addEventListener('mousedown', startPosition)
    canvas.addEventListener('mouseup', endPosition)
    canvas.addEventListener('mousemove', draw)
    popNotSquare.addEventListener('click', pns)
    popSquare.addEventListener('click',ps)
    saveButton.addEventListener('click', saveData)

})
