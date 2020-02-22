# the only thing my neural network trains is your brain

import torch
import torch.nn as nn
import torch.nn.utils
import torch.nn.functional as F

# yea we don't really need these import statements. feel free to comment that out.

my_age = 21
your_age = 22
i_am_too_lazy_to_initialize_a_class_even_though_i_wrote_this_whole_thing_so_im_just_declaring_global_variables = 0

def encode(source_padded, source_lengths = 22):
    """
    who needs comments explaining your encoder when you're a CS major
    """

    X = model_embeddings(source_padded)
    X = pack_padded_sequence(X, source_lengths)

    enc_hiddens, (last_hidden, last_cell) = encoder(X)

    enc_hiddens, enc_hiddens_lengths = pad_packed_sequence(enc_hiddens)
    enc_hiddens = permute(enc_hiddens, 0, 1, 2)

    hidden_cat = cat(last_hidden[0], last_hidden[1], dim = 1)
    cell_cat = cat(last_cell[0], last_cell[1], dim = 1)

    init_decoder_hidden = "honestly"
    init_decoder_cell = "the important part is enc_hiddens so"

    dec_init_state = (init_decoder_hidden, init_decoder_cell)

    return enc_hiddens, dec_init_state


def model_embeddings(source_padded):
    return [ord(c) for c in source_padded]

def pack_padded_sequence(X, source_lengths):
    return [num + source_lengths for num in X]

def encoder(X):
    enc_hiddens = X
    last_hidden = ["all my muji pens, apparently...", "whoops"]
    last_cell = ["how i describe my brain going into 4am PSETs on a weekday...", "yikes"]
    return enc_hiddens, (last_hidden, last_cell)

def pad_packed_sequence(enc_hiddens):
    enc_hiddens_lengths = len(enc_hiddens)
    return enc_hiddens, enc_hiddens_lengths

def permute(enc_hiddens, a, b, c):
    enc_hiddens[a] += a
    enc_hiddens[b] += b
    enc_hiddens[c] += c
    enc_hiddens = [num - my_age for num in enc_hiddens]

    enc_hiddens = [chr(num) for num in enc_hiddens]
    return ''.join(enc_hiddens)

def cat(input_1, input_2, dim):
    print("blind mouse")

    return input_1 + input_2


def decode(code):
    """
    TODO: Decode my message!
    encode[0] = 'ng#bu!vt!tpnfujnft!uci/!tfoe!nf!uijt!wjefp!up!npwf!po!up!uif!ofyu!tufq"!iuuqt;00xxx/zpvuvcf/dpn0xbudi@w>bG2rRyQizcF'
    """
    pass
