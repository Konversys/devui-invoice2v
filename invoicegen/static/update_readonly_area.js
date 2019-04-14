// Editable col = [5, 8]

function calc_readonly_data(e) {
    var row = e.id.split('r')[1].split('c')[0];
    if(e.id === strId(row, 1) || e.id === strId(row, 2) || e.id === strId(row, 3) || e.id === strId(row, 4)) {
        if ($(itemId(row, 1)).val() !== '' &&  $(itemId(row, 2)).val() !== ''
            && $(itemId(row, 3)).val() !== '' && $(itemId(row, 4)).val() !== ''){
            var result = (Number($(itemId(row, 1)).val()) + Number($(itemId(row, 2)).val())) - (Number($(itemId(row, 3)).val()) + Number($(itemId(row, 4)).val()));
            if (!isNaN(result))
                $(itemId(row, 5)).val(result);
            else
                $(itemId(row, 5)).val('Ошибка');
        }
        else
        {
            $(itemId(row, 8)).val('');
        }
    }

    if(e.id === strId(row, 1) || e.id === strId(row, 2) || e.id === strId(row, 5) || e.id === strId(row, 6) || e.id === strId(row, 7)) {
        if ($(itemId(row, 1)).val() !== '' &&  $(itemId(row, 2)).val() !== ''
            && $(itemId(row, 5)).val() !== '' && $(itemId(row, 6)).val() !== '' && $(itemId(row, 7)).val() !== '')
        {
            var result = (Number($(itemId(row, 1)).val()) + Number($(itemId(row, 2)).val())) - Number($(itemId(row, 5)).val()) - (Number($(itemId(row, 6)).val()) + Number($(itemId(row, 7)).val()));
            if (!isNaN(result))
                $(itemId(row, 8)).val(result);
            else
                $(itemId(row, 8)).val('Ошибка');
        }
        else
        {
            $(itemId(row, 8)).val('');
        }
    }
}

function strId(r, c) {
    return 'r' + r + 'c' + c
}

function itemId(r, c) {
    return '#r' + r + 'c' + c
}